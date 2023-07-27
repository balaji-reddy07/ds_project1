# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:43:51 2023

@author: Balaji reddy
"""
import glassdoor_scrapper as gs
import pandas as pd
path="E:\ds_project1\chromedriver.exe"
df = gs.get_jobs('data scientist',15,False,path,15) 