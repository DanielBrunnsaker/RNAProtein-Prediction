# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:15:14 2020

@author: Daniel Brunnsåker
"""
import pandas as pd

filename = r'F:\Downloads\RNA-Protein\RNA-Protein.txt'

chunksize = 10 ** 6

data = pd.DataFrame()

for chunk in pd.read_csv(filename, chunksize=chunksize, sep = '\t', header=None):

    temp_filtered = chunk[(chunk[4] == 'Homo sapiens') & (chunk[3] == 'mRNA') & (chunk[9] > 0.69)]
    data = pd.concat([data, temp_filtered])
    
    
    
data.columns = ['RP','SYMBOL','Entrez RNA','RNA Type', 'Species', 
                'Protein', 'Entrez Protein', 'Protein Type', 'Species', 'Confidence']


data.to_csv('homo_data.txt', sep = '\t')