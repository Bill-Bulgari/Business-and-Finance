# Stochastic Processes in Physics and Finance

This project studies Stochastic Processes using Stochastic Differential Equations, and Monte Carlo simulation, with applications in both Physics and Finance. The notebook focuses on two central stochastic models: the Ornstein-Uhlenbeck process and Geometric Brownian Motion. For each model, the project develops the Stochastic Differential Equation, Fokker-Planck equations, Euler-Maruyama simulation, and interpretation in Physics and Finance. The final section applies these ideas to Risk Management through loss distributions, Value-at-Risk, and Conditional Value-at-Risk.

## Project contents

The notebook includes:

- Itô SDEs
- Itô's lemma
- Forward and backward Fokker-Planck PDEs
- Euler-Maruyama simulation
- OU and GBM processes
- Loss distributions, VaR, CVaR
- Estimation by Order Statistics

## Repository structure

```text
Stochastic Processes in Physics and Finance
├── README.md
└── Stochastic Processes in Physics and Finance.ipynb
```

## Requirements

The project requires Python 3 and the following Python packages:

- `numpy`
- `pandas`
- `matplotlib`
- `scipy`
- `jupyter`

The notebook imports the following libraries:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
```

## Installation using pip

If you already have a working installation of Python 3, you can install the required packages using pip.

```bash
pip3 install numpy
pip3 install pandas
pip3 install matplotlib
pip3 install scipy
pip3 install jupyter
```

Alternatively, you can install all required packages with one command:

```bash
pip3 install numpy pandas matplotlib scipy jupyter
```

If `pip3` does not work on your system, you can use:

```bash
python3 -m pip install numpy pandas matplotlib scipy jupyter
```

## Purpose

The purpose of this project is to connect Stochastic Process Mathematics, Partial Differential Equations, Numerical Simulation, Physical Phenomena, and Financial Risk Analysis. It shows how continuous-time Stochastic Models can be studied analytically through SDEs or PDEs and numerically through Monte Carlo simulation.

## References

- D. T. Gillespie, “The mathematics of Brownian motion and Johnson noise,” *Am. J. Phys.* **64**, 225 (1996)
- C. W. Gardiner, *Handbook of Stochastic Methods: for Physics, Chemistry and the Natural Sciences*, Springer
- MIT OpenCourseWare, *18.642 Topics in Mathematics with Applications in Finance*, Fall 2024, Lecture Notes
