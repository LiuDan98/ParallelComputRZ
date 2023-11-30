# CS 596 project Parallel Computation and Visualization of the Riemann Zeta function

This repository contains an MPI program written in C, explorations of Zeta zeros, and related visualizations in Python. This project is for CSCI 596 course.

## Project Overview

This project uses parallel computing to explore the properties and visualizations associated with Riemann Zeta functions. The first step is to write an MPI program in C for computing Riemann Zeta sums and related performance using MPI communication functions. The second step is to visualize the Riemann functions using Python+OpenGL. The third step is to generate the corresponding zeta zeros and explore their properties using Python.

## Repository Structure

- `src`
  - `ZetaSum.c`: MPI program for batch calculating Riemann zeta sums and checking the results against the error to measure performance.
  - `ZetaSum.sl`: Scripts for processing `ZetaSum.c`, which can be handled by the user according to needs.
  - `ZetaVisualization.py`: Using OpenGL to visualize Riemann functions in the complex plane.
  - `ZetaZeros.py`: Compute and visualize the first `N` zeros of the Riemann Zeta function.
  
- `results`
  - `ZetaSum.out`: Output of `ZetaSum.c` by runinng on CARC USC.
  - `RZzeros.txt`: A file for storing the first 1000 Riemann nontrivial zeros.
  - `ZetaZeros30.png`: Distribution of the first 30 nontrivial zeros of the Riemann Zeta function.
  - `ZetaZeros1000.png`: Distribution of the first 1000 nontrivial zeros of the Riemann Zeta function.
