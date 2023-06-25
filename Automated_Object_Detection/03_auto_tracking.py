import cv2
import numpy as np
import os
import sys
import csv
import argparse
from random import randint
import datetime
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
# from pysr import PySRRegressor
# from gplearn.genetic import SymbolicRegressor
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.utils.random import check_random_state
import warnings
warnings.filterwarnings("ignore")

def smooth(x,window_len=11,window='hanning'):

    s=np.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]
    
    if window == 'flat':
        w=np.ones(window_len,'d')
    else:
        w=eval('np.'+window+'(window_len)')

    y=np.convolve(w/w.sum(),s,mode='valid')
    return y


def yolo_detection(image):

    def get_output_layers(net):
        
        layer_names = net.getLayerNames()
        try:
            output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
        except:
            output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        return output_layers


    def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):

        label = str(classes[class_id])

        color = COLORS[class_id]

        cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)

        cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    Width = image.shape[1]
    Height = image.shape[0]
    scale = 0.00392

    class_file = '../../yolo/yolov3_classes.txt'
    weights = '../../yolo/yolov3.weights'
    config = '../../yolo/yolov3.cfg'
    classes = None

    with open(class_file, 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

    net = cv2.dnn.readNet(weights, config)

    blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)

    net.setInput(blob)

    outs = net.forward(get_output_layers(net))

    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.5
    nms_threshold = 0.4


    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * Width)
                center_y = int(detection[1] * Height)
                w = int(detection[2] * Width)
                h = int(detection[3] * Height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                print
                boxes.append([x, y, w, h])


    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    # print(boxes)
    
    return boxes

def manual_detection(image):
    bbox = cv2.selectROI(image)
    print('[INFO] select ROI and press ENTER or SPACE')
    print('[INFO] cancel selection by pressing C')
    # test print coordinates of bounding box
    # print(bbox)
    return bbox

def main():
    parser = argparse.ArgumentParser(description='Detect object, extract coordinates')
    parser.add_argument('dir_name', type=str, help='dir name for video file. File should be stored as dir_name/video.mp4')


    args = parser.parse_args()
    dir_name = args.dir_name
    print(dir_name)

    if os.path.isdir(f"./experiments/{dir_name}"):
        print(f'Found directory {dir_name}. Moving there.')
        os.chdir(f"./experiments/{dir_name}")
    else:
        print(f'[ERROR] directory {dir_name} not found')
        sys.exit()
    


        
    #fname = 'trimmed_uniform_acceleration.mp4'
    fname = 'video.mp4'
    try:
        video = cv2.VideoCapture(fname)
    except:
        print('[ERROR] video file not found')
        sys.exit()
    
    print(f'[INFO] Read video file in {dir_name}')
    ret, image= video.read()

    if not ret:
        print('[ERROR] cannot read video file')
        sys.exit()

    if not os.path.exists('03_tracking_data'):
        os.makedirs('03_tracking_data')
        os.makedirs('03_tracking_data/plots')
        os.makedirs('03_tracking_data/tracking_img')
        os.makedirs('03_tracking_data/recording')

    width = image.shape[1]
    height = image.shape[0]
    scale = 0.00392

## Detection part
    bbox = []

    detection_mode = input("Detection mode: \n1. Manual Region of Interest Selection \n2.  Automatic using YOLO\n(Default 1)")

    print(f"[INFO] Detection mode {detection_mode}")
    
    if detection_mode=='':
        detection_mode = '1'

    if detection_mode == '1':
        print("[INFO] Manual detection")
        bbox = manual_detection(image)

    if detection_mode == '2':
        print("[INFO] YOLO detection")
        boxes = yolo_detection(image)
        if len(boxes) < 1:
            print('[ERROR] no object detected automatically. Switching to manual mode')
            bbox = manual_detection(image)
        else:
            print('[INFO] Object detected through YOLO')
            bbox = boxes[0]
            
    
    
    print(f"[INFO] Bounding box {bbox}")

## Tracker part

    tracker = cv2.legacy.TrackerCSRT_create()
    frame = image

    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video.get(cv2.CAP_PROP_FPS))
    video_codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    prefix = '03_tracking_data/recording/'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    basename = "object_track.mp4"
    video_output = cv2.VideoWriter("_".join([prefix, basename]), video_codec, fps, (frame_width, frame_height))

    ok = tracker.init(frame, bbox)
    if not ok:
        print('[ERROR] tracker not initialized')
        sys.exit()
    print('[INFO] tracker was initialized on ROI')

    colours = (randint(0, 255), randint(0, 255), randint(0, 255))
    # loop through all frames of video file
    i=0
    coord_list = []
    while True:
        
        ok, frame = video.read()
        if not ok:
            print('[INFO] end of video file reached')
            break

        # update position of ROI based on tracker prediction
        ok, bbox = tracker.update(frame)
        # test print coordinates of predicted bounding box for all frames

        if ok:
            (x, y, w, h) = [int(v) for v in bbox]
            coord_list.append([x, y, w, h])
            # use predicted bounding box coordinates to draw a rectangle
            cv2.rectangle(frame, (x, y), (x+w, y+h), colours, 3)
            #cv2.putText(frame, str(tracker_type), (10, 30), cv2.QT_FONT_NORMAL, 1, (255, 255, 255))
            # record object track
            video_output.write(frame)
            cv2.imwrite(f'03_tracking_data/tracking_img/traj_frame_{i}.jpg', frame)

        else:
            # if prediction failed and no bounding box coordinates are available
            cv2.putText(frame, 'No Track', (10, 30), cv2.QT_FONT_NORMAL, 1, (0, 0, 255))
        i = i+1
        # display object track
        cv2.imshow('Single Track', frame)
        # press 'q' to break loop and close window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()
    
    print("[INFO] Obtained coordinates")
    print(coord_list)

    # save coordinates to csv file



    coord_list = np.asarray(coord_list)
    np.savetxt('03_tracking_data/coord_list.csv', coord_list, delimiter=',')
    x_list = coord_list[:,0]
    y_list = coord_list[:,1]
    w_list = coord_list[:,2]
    h_list = coord_list[:,3]


    trim = -1

    win_length = 38 + (trim-1)

    x_arr = np.asarray(x_list[:trim])
    y_arr = np.asarray(y_list[:trim])
    h_arr = np.asarray(h_list[:trim])
    w_arr = np.asarray(w_list[:trim])

    center_x = (x_arr + h_arr/2)
    center_y = (y_arr + w_arr/2)

    s_x = center_x - center_x[0]
    s_y = center_y[-1] - center_y
    s_net = np.sqrt(s_x**2 + s_y**2)

    s_x = savgol_filter(s_x, win_length, 3)
    s_y = savgol_filter(s_y, win_length, 3)

    fig, (ax1, ax2,ax3) = plt.subplots(1, 3, figsize=(10, 3))

    fig.suptitle('Position')
    ax1.set_title('x')
    ax1.plot(s_x)
    ax2.set_title('y')
    ax2.plot(s_y)
    ax3.set_title('net scalar')
    ax3.plot(s_net)
    plt.savefig('03_tracking_data/plots/position.png')

    v_x = np.gradient(s_x)
    v_y = np.gradient(s_y)

    v_x = savgol_filter(v_x, win_length, 3)
    v_y = savgol_filter(v_y, win_length, 3)

    v_net = np.sqrt(v_x**2 + v_y**2)

    fig, (ax1, ax2,ax3) = plt.subplots(1, 3, figsize=(10, 3))

    fig.suptitle('Velocity')
    ax1.set_title('x')
    ax1.plot(v_x)
    ax2.set_title('y')
    ax2.plot(v_y)
    ax3.set_title('net scalar')
    ax3.plot(v_net)
    plt.savefig('03_tracking_data/plots/velocity.png')

    a_x = np.gradient(v_x,4)
    a_y = np.gradient(v_y,4)
    a_net = np.sqrt(v_x**2 + v_y**2)

    fig, (ax1, ax2,ax3) = plt.subplots(1, 3, figsize=(10, 3))

    fig.suptitle('Acceleration')
    ax1.set_title('x')
    ax1.plot(a_x)
    ax2.set_title('y')
    ax2.plot(a_y)
    ax3.set_title('net scalar')
    ax3.plot(a_net)
    plt.savefig('03_tracking_data/plots/acceleration.png')

    print("[INFO] Calculated position, velocity, and acceleration. Saved plots.")
#     print("[INFO] Running symbolic regression.")
#     a_avg = np.ones_like(a_net)*a_net.mean()
    
#     # t = np.arange(len(s_x))
#     t = np.arange(len(a_net))
#     x_var = np.stack((t,a_net)).T
#     y_var = s_net
#     sr_mode = input("Symbolic Regression mode: \n1. GPLean (Fast but complicated eqn)  \n2. PySR (Better but slow) \n(Default 1)")


    
#     if sr_mode == '2':
#         print("[INFO] Running PySR")
#         model = PySRRegressor(
#             model_selection="best",
#             niterations=40,
#             binary_operators=["*", "+", "-", "/"],
#             unary_operators=["square", 
#                             "cube",
#                 "inv(x) = 1/x",
#             ],
#             extra_sympy_mappings={"inv": lambda x: 1 / x},
#             loss="loss(x, y) = (x - y)^2",
#         )

#         model.fit(x_var, y_var)
        
#     else:
#         print("[INFO] Running GPLean")
#         est_gp = SymbolicRegressor(population_size=100,
#                             generations=10, stopping_criteria=0.01,
#                             p_crossover=0.7, p_subtree_mutation=0.1,
#                             p_hoist_mutation=0.05, p_point_mutation=0.1,
#                             max_samples=0.9, verbose=1,
#                             parsimony_coefficient=0.01, random_state=0)
#         print("Best fit:")
#         est_gp.fit(x_var, y_var)

#         print(est_gp._program)
        
#     print("[INFO] Finished symbolic regression.")

if __name__=="__main__":
    main()
