# A Visualization Workflow for Quantifying Parameter Sensitivities to Uncertainties for Hydrologic Models
## National Water Center Innovators Program: Summer Institute 2019
### Hydroinformatics Theme
Authors: [Kyla Semmendinger](mailto:kts48@cornell.edu), [Catherine Finkenbiner](mailto:finkenbc@oregonstate.edu)

### Project Overview and Workflow

![WorkFlow2](https://user-images.githubusercontent.com/20464090/61546646-6c512780-aa0f-11e9-9f74-97a50a3e7ccf.jpg)

To clone this repository to your local computer:
```
 git clone https://github.com/ksemmendinger/Hydro_Parameter_Sensitivity_Visuals.git
```

### Abstract
From regional to continental scales, models require modular components for representing individual hydrologic processes due to factors such as data availability and physical attributes. Therefore, the need for a common procedure within the hydrologic field to evaluate model output based on parameter sensitivities and uncertainties compared to performance metrics is evident. We developed a reproducible workflow for evaluating parameter sensitivities and uncertainties using the hydrologic modeling framework of the NOAA National Water Model (NWM). The NWM simulates observed and forecasted streamflow across the contiguous United States (CONUS) several times a day. High variability in soil types, elevations, vegetation characteristics, and forcings (e.g. precipitation) across CONUS leads to complexities when comparing model outputs and observed streamflow datasets. Our workflow objectively evaluates model output as a function of parameter choice using both numerical and visualization techniques. The workflow was implemented using case studies, provided by Fellows of the National Water Center Innovators Program: Summer Institute 2019. The results can be reproduced and visualized using python/R Jupyter notebooks within a community GitHub code repository. Model parameter sensitivity was evaluated using various global sensitivity indices (i.e. Sobol, delta, R2) and Bayesian theory. Uncertainty in parameter spaces were quantified to highlight the impact of unreliable input data on model output. Model parameter sensitivities and uncertainties were evaluated numerically and visually to provide a comprehensive outlook on their impacts to model output. For the case study, we provide a summary and interpretation of the workflow results. Our workflow can be integrated into hydrologic modeling frameworks for objective modular model and parameter scheme evaluations based on a data-driven approach for model selection.

Input files for the HBV, SWMM, and TOPMODEL case studies are available [here](https://drive.google.com/drive/folders/1p96I1m88nDhiwVyOoEX0ywuL5g0oBNuk?usp=sharing). To run, copy these files into the input folder within the directory of the case study.

### Dependencies

The <strong><em>environment.yml</em></strong> file is an environment for Anaconda containing the Python (v3.6.8) and R (v3.5.1) dependencies. To activate the environment, run the following in command-line:

```
conda env create -f environment.yml
conda activate si_py
```

#### Required python3 (v3.6.8) libraries:
Intall tzlocal (https://pypi.org/project/tzlocal/)
```
pip install tzlocal
```
Install rpy2 (https://rpy2.readthedocs.io/en/version_2.8.x/)
```
pip install rpy2
```
Install SALib (https://pypi.org/project/SALib/)
```
pip install SALib
```
```
import sys
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import networkx as nx
import itertools
import csv
import scipy
import SALib
import rpy2
import tzlocal
```

#### Required R (v3.5.1) libraries:
```
library(dplyr)
library(ggplot2)
library(wesanderson)
library(reshape2)
library(lattice)
library(RColorBrewer)
library(gridExtra)
library(fmsb)
library(hydroGOF)
```
