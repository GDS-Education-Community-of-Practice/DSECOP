# Module Summary

This module will connect classical Monte Carlo (MC) simulations to modern machine learning methods. Students will learn to implement Metropolis-Hastings Algorithm Ising Model simulations to generate their own 2D magnetic domain image set, then use supervised and unsupervised machine learning techniques to perform additional analysis.  Four notebooks are presented: The first is an introduction to Monte Carlo methods and Markov chains; students learn the difference between a model and a simulation, then implement basic MC integration of a differential physics equation to approximate the area under a curve.  The second notebook introduces the 2D Ising Model and the Metropolis-Hastings algorithm by teaching students how to implement the algorithm on the CPU with NumPy libraries, and GPU with TensorFlow; students will learn basic algorithm optimization techniques and generate a labeled magnetic domain image set suitable for further analysis.  The third and fourth notebooks introduce supervised and unsupervised machine learning techniques respectively; students will analyze which of the simulation parameters most strongly affected their simulation results.

### Key Words

Ising-model, Monte Carlo simulations, Markov Chains, image processing, clustering, Deep-Neural-Networks, TensorFlow, NumPy

### Courses
These notebooks are recommended for undergraduate courses in thermodynamics, solid-state physics, and computational physics, or a lab course with a computational component.

### Background Knowledge

Students should be familiar with basic probability and have beginning knowledge of a scripting language (e.g., Python, MATLAB, R, etc.).

### Estimated Amount of Time

Suggested time is 2-3 hours per notebook; total time for the module can be between 1-10 hours split between active learning during a lecture period and at-home assignments.  Notebook 1 is optional background information; subsequent notebooks do not depend on Notebook 1 content or calculations.  It is suggested that first half of Notebook 2 be completed in class to provide adequate background on the Ising Model; the second half of the notebook to be assigned as homework.  Notebooks 3 and 4 do not depend on each other but do depend on Notebook 2.

# Notebook Summary (Course Alignment Map)

|Notebook Title|Description|Data Science Learning Goals|Physics Learning Goal|
|--------------|-----------|---------------------------|---------------------|
|N1. Introduction to Monte Carlo Methods and Markov Chains | Introduces students to the difference between simulation and modeling, walks them through the steps of simulating a physical model and evaluating it| DG1. Define the difference between a model and a simulation<br><br>DG2. Define a Markov Chain<br><br>DG3. Name three error metrics.|PG1. Given a physics equation, approximate the definite integral value through Monte Carlo integration. <br><br>PG2. Given a Markov Chain, simulate the state transitions using Monte Carlo sampling.<br><br>PG3. Calculate the error between a simulation and the analytical result.|
