## Introduction to Error Reduction Techniques ##

# Module Summary
This two-module notebook consists of an introduction to sampling, interpreting, and optimizing machine learning models using mean absolute percent error (MAPE), mean standard error (MSE), and error-correcting output codes (ECOC).  This notebook can be seen as a continuation of DSECOP 150: Introduction to Classification Algorithms 
In the first module, we will explore use the of linear regression to classify types of glass based on their refractive index. From the determined classes produced, we will then implement MAPE and MSE to determine the accuracy of the model. Mean absolute percentage error measures the average magnitude of error produced by a model, or how far off predictions are on average.  This metric is an essential value for performance evaluation in data science. 
In the second notebook, students will use logistic regression to make multi-class glass data reframed as a multiple-binary classification problem using ECOC.  Classification algorithms like logistic regression are designed for two-class (binary) classification problems. ECOC is a simple yet powerful approach to deal with a multi-class problem based on the combination of binary classifiers. With this technique, the redundant “error-correcting” bits allow for some inaccuracies and can improve overall model performance. This notebook will allow students to optimize the accuracy of regression classification models using a real physics problem. 
Keywords
Error Reduction, Sci-kit learn, Matplotlib, Pandas, Classification, Introductory

# Courses #
This module would work well in a physics lab course, with little prior experience with python or coding. However, understanding basic optics, calculus, and linear algebra should be required. The level of this module is appropriate for freshman and sophomore-level students. The physics datasets are drawn from engineering physics, but in-depth physics knowledge is unnecessary. This module is directed toward lab courses that give students a hands-on understanding of the data sets from a physical perspective. 

# Physics Concepts and Objective #
The physics objectives of this module would depend on the course that this module is integrated with. The focus of this module is to be embedded within lab courses. Since classification algorithms are versatile in application, they can be applied to other physics curricula besides optics. 

# Data Science Objectives # 
This module intends to introduce students to classification techniques, such as:
•	Improve the reliability of the model by understanding error reduction techniques.
•	Distinction of classes for glass refractive index data using linear and logistic regression.
•	Apply these techniques to classify optical materials by application.
Students will become familiar with libraries such as NumPy, Pandas, matplotlib, and Scikit-Learn to enhance their classification knowledge and data visualization techniques. 

# Background Knowledge #
The module does not require much experience with python or coding. However, an understanding of introductory linear algebra and calculus-based physics should be required. Thus, this module can serve as excellent supplemental material for undergraduate physics courses for students who are in the process or have already understood the interaction of light with matter.

# Estimated Amount of Time #
It is estimated that these notebooks could be completed in a standard 2–3-hour lab.  If necessary, the linear regression module can be broken up into two (~1.5 hours) sessions, and the logistic module extended (~ 2 hours).
















