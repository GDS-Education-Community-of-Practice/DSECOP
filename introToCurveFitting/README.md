This repository contains data science educational materials developed by DSECOP Fellows.


Particle physics provides a natural avenue for applications of data science, as a large portion of cutting-edge experimentatal research is data driven. One abundant source of particle collision data is the Large Hadron Collider (LHC): in 2017, protons at the LHC were smashed together at astounding rates to produce 1 billion collisons per second [1]. These collisions produced hundreds of daughter quarks and gluons and leptons, which then collapsed to form bound states that were picked up by the detectors. Proper "detection" required storage of the particle's energy, momenta, and charge. * footnote

Sum this slew of data over the ~7 year runtime of the LHC, we're left with on the order of hundreds of petabytes of data. That's enough to fill about 1.2 million Blu-ray discs, i.e. 250 years of HD video [1]

A huge challenge is then to parse this goldmine of data into physical results. The vast majority of stored events are "common" processes, but the focus of most research is on the rarer, more interesting collisions. Further, all of the recorded data is muddled (to some degree) by detector imperfections. 

New particles or decay mechanisms are proposed, and searches for these signals are carried out. A large portion of the analysis is devoted to discriminating signal from background decays.
   
Virtually every analysis chain begins by binning a large amount of collider data into more manageable histograms, then doing the analysis on these histograms.

# Module Summary

*Students will “discover” a new particle by characterising a resonant bump in the invariant mass distribution from a set of simulated particle collisions.*

Students will be provided with a simulated dataset coming from a $pp \rightarrow X(\rightarrow ab)cd$ decay. The dataset will consist of a list the daughter particles' 4-momenta and charges. Students will plot the invariant mass of the mother particle and observe by eye a resonant “bump” corresponding to the mother particle.

Students will then write their own regression-based curve-fitting code to fit the background and resonant distributions, thus determining the mother particle mass and decay width. For a more particle physics-specific tangent, students might look into common curve-fit functions (i.e. Gaussian, Landau, Crystal Ball) and understand when a given functional form is most useful. Once students are happy with the performance of their curve-fitting tool, they will redo the analysis using scipy.optimize (which is a useful module for them to know for future research analyses).

## Learing goals
- data processing (raw data → histograms)
- curve fitting
- regression

## Relevant Packages
- NumPy
- SciPy
- Matplotlib


A summary and one or two visualizations or graphics to describe the concept What is included in this module? The following topics are expected: 

Lecture materials and hands-on lessons Quizzes Homework (Optional) other materials Which course(s) might these modules plug into? 

Physics and the data science learning goal(s) 

Estimated amount of time these might take a student to complete

Estimated amount of time these might take a professor to teach 

Pre-requisites: this section should provide what prior knowledge has been assumed in this module. This should either be from the core prerequisites or other DSECOP modules. Any other concepts should be explained. A great way would be to create a 01_intro_to_xyz.ipynb notebook and offer the required introduction. Physical concepts should be brief as our focus is on the methodology while providing additional references can guide the student to learn the concept. Up to 60% of the module can be spent on the introduction if needed. References

[1] https://home.cern/resources/brochure/knowledge-sharing/lhc-facts-and-figures
