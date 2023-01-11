#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 10:07:27 2022

@author: parisbg
"""
n = 5
one, two = 1,1

for i in range(n-5):
    temp = one
    one = one + two
    two = temp

return one