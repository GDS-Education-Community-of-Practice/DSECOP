# 03. Automated tracking

In this section, we will use the provided tracking script and pre-trained neural network to perform automated object detection and trajectory extraction. Due to some technical limitations, it is not possible to run this on colab. You don't need a gpu, just a computer with python installed.

## Environment setup

1. First clone/download this directory to your computer.

2. Set up python environment.

You can use conda or pip:

1. With conda:
On a terminal, `cd` to the cloned directory. Now run `conda env create -f environment.yml`. This will install all the prerequisites in a new conda env. Now load this env using `conda load dsecopcv`.

2. With pip
Run `pip install numpy scipy matplotlib opencv` to install the required packages. To also run the notebooks, run `pip install jupyter ipywidgets`.


3. (Optional) Download yolo weights.

Yolo is a popular neural network for image segmentation and object tracking. If your experiment has spherical objects, this might be a useful model. The weights are stored in a ~240 mb file that can be downloaded from here: [yolov3 weights](https://pjreddie.com/media/files/yolov3.weights). You can manually download the file by clicking on the link and then move it to the `yolo` directory.

If you are in the root directory of the repo, you can also run wget/curl in the terminal to download the weights to the `yolo` directory. For example, `wget https://pjreddie.com/media/files/yolov3.weights -O ./yolo/yolov3.weights`.

## Running the code

There are some examples in the `experiment` dir. However, to run the code on your own video, make a new directory `experiment_name` in the `experiment` dir. Now name your mp4 video `video.mp4` and put it in the `experiment_name` directory.

To run the code with `experiment_name`, run:
`python 03_auto_tracking.py experiment_name`.

If the video file is read correctly, you will be greeted with the following message:
```
Found directory inclined_plane. Moving there.
[INFO] Read video file in inclined_plane
Detection mode:
1. Manual Region of Interest Selection
2. Automatic using YOLO
(Default 1)
```

With option 1, we use select the object of interest, and then use an opencv tracker to get the trajectory. A window will open with the first frame of the video. Draw a box around the object of interest using your mouse and press Enter.

With option 2, we use the Yolo network. The network tries to identify the object in the video. If it is detected, then the trajectory is calculated automatically. 

We don't need yolo weights with option 1. 

 After the tracking is done, the coordinates of the object will be printed in the terminal, with the message
`[INFO] Calculated position, velocity, and acceleration. Saved plots.`

Now go to the `experiment_name` dir. The results are stored in `03_tracking_data`. The trajectory will be saved as `coord_list.csv` along with plots and recording with the bounded object.

For example, you can run 
`python 03_auto_tracking.py inclined_plane` out of the box.

## Next steps
Once you have the trajectory, you can paste it in notebook 2 and try getting its derivatives. You can also use the trajectory with the Symbolic Regression module for further analysis.