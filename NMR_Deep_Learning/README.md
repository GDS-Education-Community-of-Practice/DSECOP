# Deep Learning Applications in NMR Spectroscopy

## Summary
The Fourier transform is one of the most important concepts in signal processing. It translates an acquired signal between its time and frequency domain representations, allowing for the decomposition of a singal into its constituent frequencies, or construction of a signal from those frequencies.

The Fourier transform is used to great effect in nuclear magnetic resonance (NMR) spectroscopy, which exploits the fact that different atomic species resonate at different frequencies in a magnetic field as defined by their gyromagnetic ratio – a phenomenon known as spin precession. Faraday induction is used to detect the precession of the magnetization vector of the nuclear spins, which yields the magnetization amplitude as a function of time. The DFT decomposes this signal into discrete frequencies that may be interpreted in terms of chemical shift, which is a field-independent representation of a nucleus’s resonant frequency.

Deep learning is a sub-discipline of machine learning that encompasses the concept of neural networks. Theoretically, neural networks scale better than traditional computational methods for large amounts of data. This is particularly important for signal processing, since some datasets (e.g., magnetic resonance imaging data) can be extremely large. Deep learning algorithms attempt to learn features about the data; however, in the context of traditional computation and the DFT, the features are intrinsic to the signal. Therein arises the point of this module – can a neural network estimate the frequency content of a signal? 

## Content
These modules consists of Jupyter notebooks with homework questions meant to be evaluated with the content of the notebook. Accompanying examination material will afford instructors and students an opportunity to gauge their understanding of the content.

## Relevance
These modules are suitable for use in courses teaching content pertaining to medical physics, computational methods, image processing, and signal analysis. Some domains to which this information is useful are those of physics, chemistry, biomedical engineering, electrical engineering, and computer science.

## Pre-requisites
These modules assume prior exposure to machine learning and signal processing at an intermediate level. Introductory ML lessons may be found here [link to other fellow's notebooks with ML intro]. These modules are oriented towards physics students, so proficiency in elementary statistics is assumed.

Additional pre-requisites include a basic knowledge of Python 3.x. For advanced usage, familiarity with NumPy, SciPy, and Matplotlib is beneficial.

Due to the sheer number of parameters, notebooks are best experienced with a runtime incorporating GPU processing. Such runtimes are available by running the notebooks in a Python 3.x environment with `tensorflow-gpu` installed, or by using a hosted GPU-accelerated runtime. One such option for hosted runtimes is Google Colab.

Python environment specifications for this module are:
* Kernel
  * Python 3.x
* Modules
  * NumPy
  * SciPy
  * Matplotlib
  * Seaborn
  * Tensorflow

## Educational Content
After completing the modules, users should have increased confidence in identifying problems suitable to deep learning, engineering features, and designing network architectures with well-tunes hyperparameters. These modules seek to educate physicists and engineers on alternative problem-solving techniques in routine signal processing workloads.

## Estimated time to completion
Thorough evaluation of each module should take approximately 2 class periods to complete. Homework questions included in the modules are rigorous, requiring iterative interaction with the included networks. Most benefit from the homework questions may be achieved after 2-4 hours of experimentation with the neural networks.

## References
[1] [Bengio, Yoshua. "Practical recommendations for gradient-based training of deep architectures." Neural networks: Tricks of the trade. Springer Berlin Heidelberg, 2012. 437-478.](https://arxiv.org/abs/1206.5533)
