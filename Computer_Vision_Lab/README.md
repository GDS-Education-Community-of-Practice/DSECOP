# DSECOP 280: Computer Vision Lab
Karan Shah

-  **A summary**: This module introduces computer vision and deep learning algorithms with applications to physics problems. It covers the basics of extracting trajectories and dynamics from videos of physical phenomena, as well as how computer vision algorithms work for detection and tracking of objects. Students will gain an understanding of how information is extracted from pixels from first principles and then learn how to apply commonly used computer vision libraries. By the end of this module, participants will have an understanding of the use of computer vision and deep learning algorithms and can apply them to analyze videos from lab experiments.

The module consists of following submodules:
- 01: An introduction to image representation and manipulation with numpy. Students will implement commonly used operations on images using numpy and linear algebra.
- 02: Using the operations discussed in the previous modules, we now implement a simple object tracking algorithm to recover trajectories from lab videos. Students can run this analysis on provided examples or their own videos.
- 03: A ready-to-use python code that allows students to apply object tracking and deep learning methods on their own lab videos. This is currently available as a script that students have to run on their own computer.

-   **What is included in this module?**: The following topics are expected:
    -   Lecture materials and hands-on lessons
    -   Exercises
    -   Homework/Project
-   **Which course(s) might these modules plug into?**
	-   Introductory Classical Mechanics Lab Course (and Advanced Lab Class. Mech. experiments too)
-   **Physics and the data science learning goal(s):**
	-   Physics: Since this is a lab oriented module, students will need to think carefully how to setup experiments and capture video. Students will also learn about numerical differentiation and dealing with noise useing filters/convolutions. 

	- Data Science: 
    The module will cover the following topics:
        - How computers represent images and videos as pixels.
        - Designing image detectors and trackers from pixels using linear algebra operations.
        - Using popular CV libraries, such as OpenCV on physics videos.
        - Using deep learning models, such as Yolo for object detection.


-   **Estimated amount of time these might take a student to complete**: 6 hours
-   **Estimated amount of time these might take a professor to teach**: 2 hours
-   **Pre-requisites:** 
    - [Core prerequisites](https://github.com/GDS-Education-Community-of-Practice/DSECOP/wiki/Core-prerequisites), especially `numpy` and `matplotlib`.

This module integrates well with the Symbolic Regression module. Students can use the extracted trajectories to obtain equations using symbolic regression.

***Instructions for setting up the COLAB environment***

Click on "Open in Colab" button on any notebook. This will run the notebook on Google Colab.

Please use GPU for faster performance. You can check this by going in the "Runtime" menu in Colab, clicking on "Change Runtime Type" and setting "Hardware Accelerator" as "GPU".

***Instructions for setting up the LOCAL environment***

1. With conda:
On a terminal, `cd` to the cloned directory. Now run `conda env create -f environment.yml`. This will install all the prerequisites in a new conda env. Now load this env using `conda load dsecopcv`.

2. With pip
Run `pip install numpy scipy matplotlib opencv` to install the required packages. To also run the notebooks, run `pip install jupyter ipywidgets`.

3. (Optional) Download yolo weights.
Yolo is a popular neural network for image segmentation and object tracking. If your experiment has spherical objects, this might be a useful model. The weights are stored in a ~240 mb file that can be downloaded from here: [yolov3 weights](https://pjreddie.com/media/files/yolov3.weights). You can manually download the file by clicking on the link and then move it to the `yolo` directory.

If you are in the root directory of the repo, you can also run wget/curl in the terminal to download the weights to the `yolo` directory. For example, `wget https://pjreddie.com/media/files/yolov3.weights -O ./yolo/yolov3.weights`.