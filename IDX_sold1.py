# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:34:10 2026

@author: Emma_
"""

import pandas as pd

sold1 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202401.csv')
sold2 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202402.csv')
sold3 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202403.csv')
sold4 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202404.csv')
sold5 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202405_filled.csv')
sold6 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202406_filled.csv')
sold7 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202407_filled.csv')
sold8 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202408.csv')
sold9 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202409.csv')
sold10 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202410.csv')
sold11 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202411.csv')
sold12 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202412.csv')
sold13 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202501_filled.csv')
sold14 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202502.csv')
sold15 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202503.csv')
sold16 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202504.csv')
sold17 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202505.csv')
sold18 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202506.csv')
sold19 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202507.csv')
sold20 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202508.csv')
sold21 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202509.csv')
sold22= pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202510.csv')
sold23= pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202511.csv')
sold24= pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202512.csv')
sold25 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202601.csv')
sold26 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202602.csv')
sold27 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202603.csv')
sold28 = pd.read_csv('C:/Users/Emma_/csv/CRMLSSold202604.csv')

total_sold_before_concat = (sold1.shape[0] + sold2.shape[0] + sold3.shape[0] + sold4.shape[0] +
                           sold5.shape[0] + sold6.shape[0] + sold7.shape[0] + sold8.shape[0] +
                           sold9.shape[0] + sold10.shape[0] + sold11.shape[0] + sold12.shape[0] +
                           sold13.shape[0] + sold14.shape[0] + sold15.shape[0]+sold16.shape[0] + sold17.shape[0] + sold18.shape[0] + sold19.shape[0] +
                           sold20.shape[0] + sold21.shape[0] + sold22.shape[0] + sold23.shape[0] +
                           sold24.shape[0] + sold25.shape[0] + sold26.shape[0] + sold27.shape[0] +
                           sold28.shape[0])

combined_sold = pd.concat([
    sold1, sold2, sold3, sold4, sold5, sold6, sold7,
    sold8, sold9, sold10, sold11, sold12, sold13,sold14,sold15,sold16, sold17, sold18, sold19, sold20, sold21, sold22,
    sold23, sold24, sold25, sold26, sold27, sold28
])

print(f"Total rows from all monthly sold files BEFORE concatenation: {total_sold_before_concat}")
print(f"Total rows AFTER concatenation: {combined_sold.shape[0]}")

sold_before_filter = combined_sold.shape[0]
combined_sold_residential = combined_sold[combined_sold['PropertyType'] == 'Residential']
print(f"Rows BEFORE Residential filter: {sold_before_filter}")
print(f"Rows AFTER Residential filter: {combined_sold_residential.shape[0]}")

combined_sold_residential.to_csv('Combined_Sold_Residential_202401_202604.csv', index=False)