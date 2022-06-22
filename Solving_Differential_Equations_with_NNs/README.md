# Solving Differential Equations in Classical Mechanics with Neural Networks

## Table of Contents
* **Notebook 1: Numerical Differential Equation Solvers**: Contains explanations of Euler's method, the Euler-Cromer method, and the Velocity-Verlet method.  Also includes a worked out example of these methods applied to solving for the position of an object in freefall with drag and a prompt for students to apply these methods to solve for the motion of a simple harmonic osciallator.  This notebook can be viewed as prerequisite knowledge that could be assigned to the students as homework or covered in class at the professors choice. Filename: 01_differential_equations.ipynb
* **Notebook 2: Building a Neural Network from Scratch**: This notebook can be viewed as prerequisite knowledge that could be assigned to the students as homework or covered in class at the professors choice.
* **Notebook 3: Solving Differential Equations with Neural Networks**:  This is the main notebook for this module.  
* **Notebook 4: Further Problems**: This contains a collection of further problems that cover both the conceptual topics and coding problems covered in the above three notebooks.  These could be used as quiz, exam, or homework questions as needed. Filename: 04_further_problems.ipynb
* **Notebook 5: Solutions**: This notebook contains solutions to all of the problems posed in Notebook 4, plus any questions posed in the first three notebooks of this module.  Will be removed in the final version of this module. Filename: 05_solutions.ipynb

## Summary of Module

## Pre-requisities
* A basic knowledge of the Python programming language is assumed along with a basic knowledge of the libraries NumPy and Matplotlib.
* The ability to write down the net force equation for a given system and the knowledge of Newton's second law as well as the relationship between position, velocity, and acceleration.
* A basic knowledge of derivatives (including partial derivatives), integrals, and some basic matrix-vector manipulations.  Knowledge of differential equation is not assumed.

### Python Prerequisites
This module runs in Juupyter notebooks using the Python 3 programming languages.  Both of these need to be installed on a computer for these notebooks to run, or the notebooks can also be run on Google Colab without any local installations needed.  A link to the Google Colab versions of the noteboooks is provided at the top of each notebook. 

The Jupyter notebooks provided in this module assume that the following packages are installed.  These can be easily installed through any Python package manager such as pip3 or conda or come by default if using Google Colab.
* NumPy
* Matplotlib
* Autograd
* Scikit-Learn
* Keras

## Learning Goals

### Physics
* Be able to rewrite Newton's second law as a second order differential equation for the motion of an object
* Be able to write a Python code that solves the second order differential equation for the position of the object using Euler's method, the Euler-Cromer method, and the Velocity-Verlet Method

### Data Science
* Be able to explain how a neural network functions, including the flow of data through the network and the mathematical model for a neuron in the network
* Be able to create a small neural network by hand using Python programming and the autograd Python library.
* Be able to apply a neural network to model a given data set
* Be able to understand and explain how a neural network can be used to solve a differential equation
* Be able to edit a code for a neural network that solves a differential equation so that the parameters of the systems or different or the differnetial equation is different    

## Suggested Course to Plug Into

The material contained in this module was designed to work with a classical mechanics course, typically being a course taught to sophomore level college students or above.  The material contained in Notebook 1 does not go above the level usually taught at in an introductory mechanics course (assume drag is at least minimally covered), but some of the mathematics contained in Notebooks 2 and 3 may be difficult for students who have not taken more advanced calculus courses (partial derivatives, etc).

## Time Needed for Students to Complete the Assignments: 6+hr
It is estimated that a student will need 2 hours each to complete Notebooks 1-3 and the estimated times to complete the extra problems contained in Notebook 4 are supplied per problem.  However, depending on a student's Python knowledge, more time may be needed to fully understand the coding aspects of the notebooks.

## Time Needed for Professors to Teach the Material: 2+hr

It is estimated to cover just Notebook 3 in class would take 2 class periods (assuming a 50 minute class period).  If the professor chooses to teach Notebooks 1 and 2 as part of the regular class as well it is estimated that Notebook 1 would take 1 50 minute class period and Notebook 2 would take 2 50 minute class periods, though these two notebooks can also be viewed as prerequisites and assigned as homework/out of class work for the students.

## References

