Author: Joseph Dominicus Lap
E-mail: joseph.dominicus.lap@yale.edu
# Introduction to Symbolic Regression
The aim of this module is to introduce students to symbolic regression, multi-step algorithms, and how concepts from physics can be useful in a datscience context. It does this by introducing them to the 2020 [AIFeynman algorithm](https://www.science.org/doi/10.1126/sciadv.aay2631). Symbolic regression is not just a method of fitting data to a model, but rather a method of model discovery. It aims to find the mathematical expression that best fits the form of the data. The AIFeynman algorithm accomplishes this efficiently by using tricks from physics such as dimensional analysis, additive/multiplicative seperability, and translational symmetry. Due to the modularity of the algorithm, the notebook is correspondingly modular and educators should feel free to use only the portions relevant to their course.

## Learning Goals
The objective is to get a sense of the various techniques physicists use to simplify problems. Ones covered include:
• Dimensional Analysis
• Symmetry (an intuitive grasp without delving into group theory)
• Separability

After this module one should be able understand all the steps in a multi-step algorithm, understand how noisy data effects algorithms, and *optionally* be able to understand and apply small neural networks

## Prerequisites
A basic understanding of ```numpy```, ```matplotlib```, and ```pandas``` will be necessary to understand the functioning of the notebook. In addition linear algebra will be necessary to understand the dimensional analysis algorithm.
*Optional*: In order to delve into the functioning of the neural network one should have experience with ```PyTorch``` and Neural Networks, which can be gained from the [Intro to Deep Learning module](../Intro_to_Deep_Learning/).

## What's included in this module?
The main notebook is ```01_Symbolic_regression.ipynb```. It will walk students through the different parts that make up the AI Feynman algorithm and has several conceptual exercises so they can confirm their understanding. In addition there's ```02_NeuralNet.ipynb``` which allows students to look under the hood of the neural network used in the symbolic regression notebook. More advanced courses can tweak the network (change loss functions, tune hyperparameters, make it deeper, etc.) and see how this effects the algorithm's functioning.

## What courses might this module accompany?
This model would fit nicely into a lab course. The pared down version can be used for more introductory labs and more senior versions can make use of the additional neural network material. Data from the lab can be run through the algorithm, but “sample data” will be provided that is generated from a known equation so that the pedagogy doesn’t depend on amount of data or precision of data (it is estimated that the algorithm is 50% less effective with even 1% error).
Additionally if one is covering non-ohmic resistivity in an undergraduate Electromagnetism class, the notebook can be used to discover various non-ohmic expressions for the voltage as a function of current and resistance.

## Time Estimation
It's estimated that each section of ```01_Symbolic_Regression.ipynb``` will take 30 minutes for a total of 3 hours. An additional 1 hour should be scheduled for allowing the students to play with different datasets. *Optionally* an additional 1-2 hours for digging into the workings of the Neural Network.
