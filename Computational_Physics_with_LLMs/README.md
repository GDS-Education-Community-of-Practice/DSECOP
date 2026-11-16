# Computational Physics with LLMs

[https://github.com/user-attachments/assets/VIDEO_ID](https://github.com/user-attachments/assets/33283630-7d05-49d4-bc85-e857b9a56755
)

*Example output from Route A1. The uniform cloud from Section 3 (left) and a clumpy cloud (middle) collapse side by side, while the validation panel (right) tracks the half-mass radius and the width of the local density distribution against dashed analytic references. Your movie will differ in its details, and working out what the curves mean is part of the exercise.*

This module teaches undergraduate physics students to design, validate and extend a computational physics code with an AI coding assistant. Students work in a Jupyter notebook inside VS Code with an LLM (in this case Claude Code) docked beside it. They build an N-body simulation of a cold molecular gas cloud collapsing under its own gravity, the first step toward forming a young star cluster, and then extend it along one of three routes focused on classical mechanics, statistical mechanics and thermodynamics, or computational physics.

The collapsing cloud is the specific example used in this instance; the skill being taught is the code development and validation workflow. Students drive the work with prompts, answer the assistant's clarifying questions about the integrator, initial conditions, gravitational softening and simulation parameters, run the simulations, and turn the results into movies. Every feature comes with a validation panel that compares the simulation with an analytic prediction to verify simulation results. Deriving that prediction, stating what it assumes, and explaining where the simulation departs from it is the students' job, done together with the assistant.

### Courses

The primary target audiences are undergraduate classical mechanics (Route A), statistical mechanics and thermodynamics (Route B), and computational physics (Route C) students. The module is also suitable for an introductory astrophysics course or a computational lab.

### Background Knowledge

Basic Newtonian gravity, conservation of energy and angular momentum, and some Python. Route B builds on the ideal gas and adiabatic processes; Route C on the idea of algorithmic complexity (big-O notation). No prior experience with N-body codes, numerical integrators or animation is needed: the assistant writes the code, and the notebook explains the physics.

### Estimated Amount of Time

Do the setup (Section 0) before class. In a class period, build the base code (Section 3) and then follow Route A, whose features take about 5–10 minutes each. Route B and Route C features take about 20 minutes each and are suggested for home. Each simulation run and movie render takes several minutes.

# Notebook Summary

| Section | What students do | Computational learning goals | Physics learning goals |
|---------|------------------|------------------------------|------------------------|
| 0. Setup | Install VS Code with the Python, Jupyter and Claude Code extensions, ffmpeg and a Python 3.11+ environment, and dock Claude beside the notebook. | Set up a reproducible environment and work with an AI assistant inside VS Code. | |
| 1–2. Introduction and physics overview | Read the physics of the collapse, the three routes, and how every feature will be validated. | Understand what validating a simulation means and why a code that runs is not necessarily correct. | N-body gravity with softening, leapfrog integration, the Jeans mass and free-fall time, the virial theorem, angular momentum, density clumping, polytropes, SPH, sink particles, and the cost of direct versus tree force calculations. |
| 3. Base N-body code | Prompt the assistant for a simple N-body code of a cold cloud that writes snapshots, a script that turns them into a 3D movie, and a first run with a validation panel; list the code's limitations compared with research-grade codes; prepare the code for modular features. | Specify a simulation through prompts and clarifying questions; write snapshot output and visualizations; validate against an analytic reference; critique a code's design choices. | Self-gravitating collapse of a cold, uniform sphere; how the integrator, softening and initial conditions shape the result; the half-mass radius as a collapse diagnostic. |
| Route A: Classical mechanics (A1–A3) | Add a clumpy initial density, rotation (toward disk formation), or an artificial virial ratio, and compare each run side by side with the base run. | Add features as flags; run controlled comparisons with identical numerical settings; plot conserved quantities honestly. | Fragmentation and local free-fall times; angular momentum and the centrifugal barrier; kinetic support and the virial theorem. |
| Route B: Statistical mechanics and thermodynamics (B1–B2) | Give the gas an equation of state that links density to temperature, with smooth-particle hydrodynamic pressure forces; then add sink particles (protostars) that accrete gas and heat their surroundings. | Estimate densities from particles; add a new force to an existing integrator; keep track of energy and mass bookkeeping. | Compressional heating and pressure support; gravitational stability; sink formation, accretion and feedback. |
| Route C: Computational physics (C1) | Replace the direct force sum with a vectorized Barnes–Hut tree, run timing tests with up to ten times more particles, and plot runtime against N with the theoretical scalings and fitted exponents. | Tree data structures, vectorizing an algorithm, benchmarking, fitting scaling exponents, and measuring accuracy against a reference method. | Approximating distant mass by its centre of mass, and the trade-off between accuracy and cost. |
| 4. Comparison and wrap-up | Stack features, explore parameters such as the particle number or the opening angle, and ask for extra diagnostics. | Design your own experiments with the assistant. | How collapse outcomes depend on the physics included and on the numerical parameters. |

## Validation: deriving the reference is the exercise

Every feature produces a **validation panel**: in the movie it animates alongside the 3D views and plots measured quantities against analytic predictions drawn as dashed targets. The primary quantity is always the **half-mass radius**; each feature adds a secondary quantity on a right-hand axis.

| Feature | Secondary quantity |
|---------|--------------------|
| Base code | mass–radius concentration ratio |
| A1 clumpy density | width of the local density distribution |
| A2 rotation | total angular momentum |
| A3 virial ratio | virial ratio |
| B1 equation of state | total energy, including internal energy |
| B2 sink particles | sink mass fraction, and total mass |
| C1 Barnes–Hut | fitted scaling exponent (timing tests, no movie) |

The notebook ships no validation library and quotes no expected numbers. For each quantity, ask the assistant to derive the analytic prediction from first principles, state the assumptions it rests on, and say where those assumptions stop holding. Then read the result the right way round: the base run should follow its reference until those assumptions fail, and each feature run should depart from it in a way you can explain physically. When a check fails, suspect the simulation first, but check the derivation too.

## How to Run

1. Follow Section 0 of the notebook. Install [VS Code](https://code.visualstudio.com/) with the Python, Jupyter and Claude Code extensions, plus ffmpeg and Python 3.11 or newer. Open this folder (not just the notebook) in VS Code and turn on **File → Auto Save**. Create a `.venv` environment, run `pip install ipykernel numpy matplotlib` in its terminal, and select it as the notebook kernel. Dock Claude with **Claude Code: Open in Side Bar** and sign in.
2. Open `gas_cloud_collapse.ipynb` and run the environment check cell.
3. Work through the prompts in order, typing each one into the Claude panel. Claude asks clarifying questions and suggests defaults: accept them or explore alternatives. Claude writes the code into the notebook cells (and the scripts they create) and launches long runs in the VS Code terminal; you run the cells yourself with Shift+Enter.
4. Before starting a route, give the context prompt in Section 3.5, so that each feature becomes a switchable flag and each new run is compared side by side with the base run using identical settings.

Simulation snapshots appear under `simulations/<run name>/` and movies under `movies/`.

The notebook was tested with Claude's latest Opus model (1M context) at maximum effort, and those settings are recommended: the model and effort level affect what you get.

## Materials

- `gas_cloud_collapse.ipynb`: the student notebook, with the setup, the physics background, and the prompts for every section and route. Its code cells are placeholders for the assistant to fill.
- `CLAUDE.md`: project instructions that Claude Code reads automatically. They make it ask clarifying questions before adding physics, explain its choices, derive validation references from first principles, and report a failed check for you to investigate instead of explaining it away. Keep this file in the folder.
