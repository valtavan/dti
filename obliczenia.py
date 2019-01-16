# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 23:47:26 2019

@author: Stanisław Narębski
"""

import numpy as np
from pathlib import Path

p = Path('.')

avg = np.zeros((97,97))
n   = 0

for path in p.glob('*.txt'):
    #print(path)
    curr = np.loadtxt(path)
    avg += curr
    n   += 1
    
avg = avg/n

np.savetxt('avg.txt', avg)
