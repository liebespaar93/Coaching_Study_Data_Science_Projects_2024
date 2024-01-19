#!/usr/bin/env python
# coding: utf-8

## version
# !if [ $(pip list | grep "seaborn" | awk '{ print $2 }' | awk 'NR < 2') != 0.13.1 ]; then pip install seaborn==0.13.1; fi
# !if [ $(pip list | grep "matplotlib" | awk '{ print $2 }' | awk 'NR < 2') != 3.8.2 ]; then pip install matplotlib==3.8.2; fi

import pandas as pd
import pandas.core.frame
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt