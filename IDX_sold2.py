# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:22:05 2026

@author: Emma_
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your dataset
sold = pd.read_csv("C:/Users/Emma_/IDX exchange/Combined_Sold_Residential_202401_202604.csv")

# Set plot style for readability
plt.style.use("seaborn-v0_8-whitegrid")

#inspect column and rows
print("Dataset Shape (rows, columns):", sold.shape)
print(sold.head)
print(sold.dtypes)

#Analysis martjet field
market_fields=["ClosePrice", "ListPrice", "OriginalListPrice", "LivingArea",
    "LotSizeAcres", "BedroomsTotal", "BathroomsTotalInteger",
    "DaysOnMarket", "YearBuilt", "PropertyType", "County",
    "ListDate", "CloseDate"]

market_data=[col for col in sold.columns if col not in market_fields]

print(market_data)
print(market_fields)

#check property
print(sold['PropertyType'].unique() )

#filter residential 
sold = sold[sold.PropertyType == 'Residential']

#Missing values
missing_counts = sold.isnull().sum()
missing_pct = (sold.isnull().sum() / len(sold)) * 100

missing_summary = pd.DataFrame({
    "Missing Count": missing_counts,
    "Missing %": round(missing_pct, 2)
})
missing_summary = missing_summary.sort_values("Missing %", ascending=False)

print("\n--- Full Missing Value Summary ---")
print(missing_summary)
high_missing_cols = missing_summary[missing_summary["Missing %"] > 90].index.tolist()
print(f"\nColumns with >90% missing values (to consider dropping): {high_missing_cols}")

#Numeric distribution review
numeric_cols = [
    "ClosePrice", "ListPrice", "OriginalListPrice", "LivingArea",
    "LotSizeAcres", "BedroomsTotal", "BathroomsTotalInteger",
    "DaysOnMarket", "YearBuilt"
]
print(sold[numeric_cols].describe(percentiles=[.01, .1, .25, .5, .75, .9, .99]))

for col in numeric_cols:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Histogram
    sold[col].hist(ax=ax1, bins=40)
    ax1.set_title(f"Histogram: {col}")
    ax1.set_xlabel(col)
    ax1.set_ylabel("Count")
    
    # Boxplot to spot outliers
    sold.boxplot(column=col, ax=ax2)
    ax2.set_title(f"Boxplot: {col} (Outlier Detection)")
    
    plt.tight_layout()
    plt.show()

# Identify extreme outliers (99th / 1st percentile cutoff example)
outlier_summary = {}
for col in numeric_cols:
    p1 = sold[col].quantile(0.01)
    p99 = sold[col].quantile(0.99)
    outliers = sold[(sold[col] < p1) | (sold[col] > p99)]
    outlier_summary[col] = f"{len(outliers)} outliers outside 1%-99% range"

print("\n--- Outlier Counts per Numeric Field ---")
for k, v in outlier_summary.items():
    print(f"{k}: {v}")




