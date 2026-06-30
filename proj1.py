#!/opt/anaconda3/bin/python3

# EECE 5644 - Machine Learning
# Skylar Denno
# June 30, 2026

# MINI PROJECT 1

import sys, subprocess
def pipq(*pkgs):
    subprocess.run([sys.executable, "-m", "pip", "-q", "install", *pkgs])

pipq("scikit-learn", "pandas", "numpy", "matplotlib", "seaborn")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns", 60)
np.random.seed(0)

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

df = pd.read_csv("data.csv", encoding="ISO-8859-1")
print("Loaded dataset with", df.shape[0], "rows")
print(df.head())


