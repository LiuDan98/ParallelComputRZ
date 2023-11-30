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

## Riemann Zeta function

### Introduction

The Riemann Zeta Function, typically denoted by the Greek letter `ζ` (Zeta), is a special function defined on the complex plane. It was introduced by the German mathematician Bernhard Riemann in 1859 and has been extensively studied, spanning various fields such as mathematics, physics, and engineering. A famous conjecture related to the Riemann Zeta Function is the Riemann Hypothesis. It posits that the non-trivial zeros of the function (those not corresponding to negative integers) lie on the critical line in the complex plane with the real part equal to $\frac{1}{2}\$. Despite extensive attention, this hypothesis remains unproven. 

The Riemann Zeta function plays a crucial role in mathematics, particularly in connection with number theory and complex analysis, exerting a profound influence on topics such as prime number distribution. In the realm of physics, it appears in quantum field theory and statistical physics, serving as a key tool for studying issues like energy level distribution and regularization.

### Analytic Form on the Complex Plane

The analytic form of the Riemann Zeta Function on the complex plane is defined as follows:

$\zeta(s) = 1^s + 2^{-s} + 3^{-s} + 4^{-s} + \ldots$

where `s` is a complex number. Specifically, if $s = a + bi$, then

$\zeta(s) = 1^s + 2^{-s} + 3^{-s} + 4^{-s} + \ldots$

In certain regions, this series converges, providing the definition of the Riemann Zeta Function in that region.



