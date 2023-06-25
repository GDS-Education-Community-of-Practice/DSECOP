# Time Series Analysis and Forecasting Applied to Projectile Motion with Drag
Connor Robertson

## Summary
This module is meant to teach basic time series analysis and forecasting along with the use of recurrent neural networks for time series forecasting. 
Though the material is generally applicable to a wide range of fields and career paths, it is presented in the context of projectile motion with drag. 
As such it is well suited to a course on classical mechanics. The module is split into three standalone submodules:

- **Notebook 1** (2 hr): Simulating projectile motion without and with drag 
![Notebook 1](images/projectile_motion.gif)

- **Notebook 2** (2 hr): Analyzing and forecasting noise polluted trajectory data from notebook 1 using standard time series techniques
![Notebook 2](images/timeseries_metrics.png)

- **Notebook 3** (1 hr): Forecasting projectile motion using recurrent neural networks trained on trajectory data from notebook 1
![Notebook 3](images/timeseries_forecast.png)
    
Though the submodules build on each other and are interrelated, they can be done individually or in any pair.
Each submodule contains 3-4 programming questions that allow the students to modify example code to better understand how the program in these contexts and to explore the effects of different models and parameters.


 
<!-- ![Time evolution for a 1D Quantum Harmonic Oscillator](res/plots/waveform/psi_1_3/animation.gif) -->
## Learning Goals
*Python packages that students will use for goals are listed `as such`.*

### Physics
- To be able to write out the equations for projectile motion with drag as a first order differential equation
- To be able to simulate the motion of the projectile (`scipy`)
- To understand the influence of different components of the drag force on the projectile motion (notably linear vs. quadratic influence)

### Data Science

- To be able to use interactive visualization to explore data (`matplotlib`, `ipywidgets`, `jupyter`)
- To be able to manipulate, save, and load tabular data (`pandas`)
- To be able to examine, analyze, and visualize time series data using common metrics (`numpy`, `pandas`, `matplotlib`, `statsmodels`)
- To be able to forecast future times series states with the ARIMA linear models and univariate data (`statsmodels`)
- To be able to forecast future time series states with a recurrent neural network and multivariate data (`keras`)

## Prerequisites
- Python programming as listed in the [core prerequisites](https://github.com/GDS-Education-Community-of-Practice/DSECOP/wiki/Core-prerequisites)
- Students will require familiarity with Newton's second law and ordinary differential equations

Having an understanding of the `pandas` Python package would be helpful.
Additionally, a basic understanding of neural networks would help with the submodule on forecasting with recurrent neural networks.
As a resource for this, the [Intro to Deep Learning](https://github.com/GDS-Education-Community-of-Practice/DSECOP/tree/main/Intro_to_Deep_Learning) module may be helpful.

## Setup Instructions
	
***Instructions for setting up the COLAB environment***

Click on "Open in Colab" button on any notebook in this repository.
This will run the notebook on Google Colab.

***Instructions for setting up the LOCAL environment***
To set up the environment with conda:

1. Create new environment using the `environment.yml` file in this repository:
`conda env create -f environment.yml`
2. Activate the env:
`conda activate timeseries`
3. Run `jupyter notebook` in this directory. A browser window will open where the notebooks can be viewed.
