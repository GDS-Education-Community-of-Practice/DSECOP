# Introduction to Data Processing

A key component of scientific research is the *analysis pipeline*, the analytical and computational steps that convert a dataset of raw measurements into meaningful results. The process of extracting relevant features from long tables of numbers is a sort of art form, as there is ambiguity at every step: how should one determine what parameters of a given model best fit the data? Or how can one establish confidence that their preferred model is in fact the one that best describes the data?



<img align="left" width="400" height="350" 
src="https://drive.google.com/uc?export=view&id=13I4wekAVCOYpGFE2uJRR0B9gOIDr2JBE">


In this module, students will be introduced to common steps in an analysis pipeline. They will gain practice in processing datasets into more compact histograms and curve fitting the distributions to possible underlying models. Students will also learn how to quantify how well a hypothesized matches the true model that produced the dataset. 

## Learning goals

After completing these modules, students should feel comfortable:

(Physics Goals)
- using histograms as a tool to visualize large datasets
- evaluating how well a given model fits a dataset
- constructing their own analysis pipelines

(Data Science Goals)
- using built-in functions from ```numpy``` and ```scipy``` to produce histograms from a dataset
- using built-in functions from ```numpy``` and ```scipy``` to curve fit a distribution
- writing their own code to do any of the above tasks, if desired

## Prerequisites

Students are expected to be familiar with ```python```, ```numpy```, and  ```matplotlib```. 

## What's included in this module?

### In-class modules

Three in-class modules will guide students through the analysis of the radioactive decays of a toy “Uranium-241” sample. The modules will cover:
- creating histograms from large datasets (```01_introduction_to_histograms.ipynb```)
- curve fitting analytical models to histograms (```02_introduction_to_curve_fitting.ipynb```)
- evaluating how well a fit model describes the dataset (```03_goodness_of_fit.ipynb```)

Estimated time to complete: 30 minutes per module 

### Conceptual Quiz Questions

A short quiz will provide problems to students that challenge implicit assumptions they might have developed while completing the modules.

Estimated time to complete: 20 minutes 

### Homework Assignment

The homework assignment is a realistic data analysis task that draws upon the material introduced in the in-class modules. 

Students will be given a dataset of $ee \rightarrow abcd$ collisions. They will be told that the decay particles are produced through a mystery particle $X$. They will be guided through a full analysis pipeline to determine the mass of the mystery particle, including:
- calculating and histogramming $m_X$ candidates 
- fitting the distribution, and 
- comparing their recovered value of $m_X$ with the value that their “theorist friend” has predicted.

Estimated time to complete: 60 - 90 minutes 

### Datasets

Several datasets are provided to accopany these modules. We also provide ```iPython``` notebooks for instructors to re-generate the datasets, if they wish to change any of the relevant parameters.

The notebook ```data_generation.ipynb``` creates:
- (for the in-class modules) two files (```geiger_counts_A.txt``` and ```geiger_counts_B.txt```) containing a few thousand Poisson distributed values, meant to represent the number of clicks heard per minute from a Geiger counter placed near the sample.
- (for the quiz questions) one file ```quiz_dataset.txt``` contains of a generic signal (gaussian, 3000 events) + background (exponential, 5000 events) dataset.

The notebook ```homework_dataset_generation.ipynb``` creates:
- (for the homework) one file ```ee_collisions.txt``` containing a sample of 10,000 simulated $ee \rightarrow abcd$ collisions. The dataset contains four-momenta and charge information for each daughter particle. 
*You must have* ```pyROOT``` *installed to be able to run this notebook.*


## What courses might these modules accompany?

These modules might be shown in the first two weeks of an undergraduate laboratory course. Additionally, the homework could be given as a standalone assignment for an undergraduate Particle Physics course.

### TODO
- [ ] Image for ReadMe Pipeline
- [ ] Module 1: Other data visualizations (i.e. scatter plots, time series)
- [ ] Module 3: Confidence Intervals + residual pull plots
- [x] Module 3: KS test actually can't be used for a discrete Poisson distribution...can the module still work for teaching purposes??
- [ ] Module 4: (From scratch) deep learning Higgs detection

