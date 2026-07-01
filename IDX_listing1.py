# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:41:18 2026

@author: Emma_
"""
import pandas as pd

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







