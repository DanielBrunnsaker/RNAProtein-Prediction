# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:15:14 2020

@author: Daniel Brunnsåker
"""
import pandas as pd

filename = r'C:\Users\Daniel Brunnsåker\Desktop\RNA\homo_data.txt'

data = pd.read_csv(filename, sep = '\t', header=None)
