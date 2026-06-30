############################################################

# EECE 5644 - Machine Learning
# Skylar Denno
# June 30, 2026

# MINI PROJECT 1
# Data cleaning and data preprocessing

############################################################

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

############################################################

# CLASS TO PRINT BASIC INFORMATION OF DATASET
class DataInfo:

    def __init__(self, df):
        self.df = df

    def set_df(self, df):
        self.df = df
        return self.df
    
    # method to print getting information results
    # print_basic_description() : Dataframe -> Print Output
    def print_basic_description(self):
        print("\n\n--------------------\nBASIC DESCRIPTION\n--------------------")
        print("\nLoaded dataset with", self.df.shape[0], "rows")
        print("\nShape:", self.df.shape)
        print("\nColumns:", list(self.df.columns))
        print("\nInfo:", self.df.info())
        print("\nStatistical Description:", self.df.describe())
        print("\nHead (first 10 rows):", self.df.head(10))

    # method to print some unique values/counts
    # print_unique_values() : Dataframe -> Print Output
    def print_unique_values(self):
        print("\n\n--------------------\nUNIQUE VALUES/COUNTS\n--------------------")
        print("\nNum. of instances of each country present: ", self.df["Country"].value_counts())
        print("\nNum. of unique Stock Codes: ", self.df["StockCode"].nunique())
        print("\nNum. of unique product descriptions:", self.df["Description"].nunique())

    # method to print Min/max/sum/mean/count for selected numeric columns
    # print_numeric_summary() : Dataframe -> Print Output
    def print_numeric_summary(self):
        print("\n\n--------------------\nNUMERIC SUMMARY\n--------------------")
        summary = self.df[["Quantity", "UnitPrice"]].agg(["min", "max", "sum", "mean", "count"])
        print(summary)

############################################################

# CLASS WITH METHODS TO CLEAN DATA
class DataClean:

    def __init__(self, df_raw=None, df_clean=None):
        self.df_raw = df_raw
        self.df_clean = df_clean
        self.country_region_lookup = None

    # getter for raw df
    def set_raw(self, df):
        self.df_raw = df
        return self.df_raw

    # getter for clean df
    def set_clean(self, df):
        self.df_clean = df
        return self.df_clean

    # build lookup table for country to region mapping
    # build_country_region_lookup() : [Call] -> Dict
    def build_country_region_lookup(self):
        country_region_data = [
            ("United Kingdom", "UK & IE"),
            ("Germany", "Western Europe"),
            ("France", "Western Europe"),
            ("Spain", "Western Europe"),
            ("Netherlands", "Western Europe"),
            ("Belgium", "Western Europe"),
            ("Switzerland", "Western Europe"),
            ("Portugal", "Western Europe"),
            ("Australia", "Oceania"),
            ("Norway", "Northern Europe"),
            ("Italy", "Southern Europe"),
            ("Channel Islands", "Western Europe"),
            ("Finland", "Northern Europe"),
            ("Cyprus", "Mediterranean"),
            ("Sweden", "Northern Europe"),
            ("Austria", "Western Europe"),
            ("Denmark", "Northern Europe"),
            ("Japan", "Asia Pacific"),
            ("Poland", "Central Europe"),
            ("Israel", "Middle East"),
            ("USA", "North America"),
            ("Hong Kong", "Asia Pacific"),
            ("Singapore", "Asia Pacific"),
            ("Iceland", "Northern Europe"),
            ("Canada", "North America"),
            ("Greece", "Southern Europe"),
            ("Malta", "Southern Europe"),
            ("United Arab Emirates", "Middle East"),
            ("Lebanon", "Middle East"),
            ("Lithuania", "Eastern Europe"),
            ("Brazil", "South America"),
            ("Czech Republic", "Central Europe"),
            ("Bahrain", "Middle East"),
            ("Saudi Arabia", "Middle East"),
            ("RSA", "Africa"),
            ("European Community", "GENERAL EUROPE"),
            ("Unspecified", "UNSPECIFIED"),
        ]

        country_region_dict = dict(country_region_data)
        country_region_dict.setdefault("DEFAULT", "INVALID COUNTRY")

        self.country_region_lookup = country_region_dict
        return self.country_region_lookup

    # iloc slice rows
    # slice_rows(df) : DataFrame -> DataFrame
    def slice_rows(self, df):
        df = df.copy()
        df.index = [f"item_{i}" for i in range(len(df))]

        print("\n\n--------------------\nSLICING WITH ILOC AND LOC\n--------------------")
        print("\nFirst 5 rows with iloc:")
        print(df.iloc[0:5])
        return df

    # remove rows with invoice numbers starting with 'C' (canceled orders)
    # remove_canceled_orders(df) : DataFrame -> DataFrame
    def remove_canceled_orders(self, df):
        df = df.copy()
        df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
        return df

    # puts the largest orders (high qty) at top
    # find_largest_orders(df) : DataFrame -> DataFrame
    def find_largest_orders(self, df, top_n=5):
        df = df.copy()
        df["LineRevenue"] = df["Quantity"] * df["UnitPrice"]

        print("\n\n--------------------\nTOP BULK ORDERS BY QUANTITY\n--------------------")
        print(df.sort_values("Quantity", ascending=False).head(top_n)[["InvoiceNo", "StockCode", "Description", "Quantity", "UnitPrice", "LineRevenue"]])

        print("\n\n--------------------\nTOP ORDERS BY LINE REVENUE\n--------------------")
        print(df.sort_values("LineRevenue", ascending=False).head(top_n)[["InvoiceNo", "StockCode", "Description", "Quantity", "UnitPrice", "LineRevenue"]])

        print("\n\n--------------------\nTOP RETURNS BY NEGATIVE QUANTITY\n--------------------")
        returns = df[df["Quantity"] < 0]
        print(returns.sort_values(["Quantity", "LineRevenue"], ascending=[True, True]).head(top_n)[["InvoiceNo", "StockCode", "Description", "Quantity", "UnitPrice", "LineRevenue"]])

        return df.sort_values(["Quantity", "LineRevenue"], ascending=[False, False])

############################################################

pd.set_option("display.float_format", "{:.3f}".format)

# load raw data
raw_df = pd.read_csv("data.csv", encoding="ISO-8859-1")
# create a copy to clean (keeping a copy of raw)
clean_df = raw_df.copy()
clean_df = clean_df.dropna(subset=["CustomerID", "Description"])

di = DataInfo(raw_df)  # instantiate
di.print_basic_description()
di.print_unique_values()
di.print_numeric_summary()

dc = DataClean(df_raw=raw_df, df_clean=clean_df)

country_region_lookup_table = dc.build_country_region_lookup()
clean_df = dc.slice_rows(clean_df)

clean_df = dc.remove_canceled_orders(clean_df)

clean_df = dc.find_largest_orders(clean_df)

di_clean = DataInfo(clean_df)
di_clean.print_basic_description()