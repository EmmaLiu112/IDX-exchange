# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 04:59:05 2026

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


list2 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202402.csv')
list3 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202403.csv')
list4 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202404.csv')
list5 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202405.csv')
list6 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202406.csv')
list7 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202407.csv')
list8 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202408.csv')
list9 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202409.csv')
list10 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202410.csv')
list11 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202411.csv')
list12 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202412.csv')
list13 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202501.csv')
list14 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202502.csv')
list15 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202503.csv')
list16 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202504.csv')
list17 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202505.csv')
list18 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202506.csv')
list19 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202507.csv')
list20 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202508.csv')
list21 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202509.csv')
list22 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202510.csv')
list23 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202511.csv')
list24 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202512.csv')
list25 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202601.csv')
list26 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202602.csv')
list27 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202603.csv')
list28 = pd.read_csv('C:/Users/Emma_/csv/CRMLSListing202604.csv')

# Sum all individual file row counts
total_list_before_concat = (list2.shape[0] + list3.shape[0] + list4.shape[0] + list5.shape[0] +
                           list6.shape[0] + list7.shape[0] + list8.shape[0] + list9.shape[0] +
                           list10.shape[0] + list11.shape[0] + list12.shape[0] + list13.shape[0] +
                           list14.shape[0] + list15.shape[0] + list16.shape[0] + list17.shape[0] + list18.shape[0] + list19.shape[0] +
                           list20.shape[0] + list21.shape[0] + list22.shape[0] + list23.shape[0] +
                           list24.shape[0] + list25.shape[0] + list26.shape[0] + list27.shape[0] +
                           list28.shape[0])

# Concatenate all monthly listing data
combined_list = pd.concat([
    list2, list3, list4, list5, list6, list7,
    list8, list9, list10, list11, list12, list13, list14, list15, list16,
    list17, list18, list19, list20, list21, list22,
    list23, list24, list25, list26, list27, list28
])

# Print row comparison checks
print(f"Total rows from all monthly listing files BEFORE concatenation: {total_list_before_concat}")
print(f"Total rows AFTER concatenation: {combined_list.shape[0]}")

# Filter only Residential properties
list_before_filter = combined_list.shape[0]
combined_list_residential = combined_list[combined_list['PropertyType'] == 'Residential']
print(f"Rows BEFORE Residential filter: {list_before_filter}")
print(f"Rows AFTER Residential filter: {combined_list_residential.shape[0]}")

# Export final combined listing file
combined_list_residential.to_csv('Combined_Listing_Residential_202402_202604.csv', index=False)







