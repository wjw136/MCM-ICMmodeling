import pandas as pd
import numpy as np
import matplotlib as plt
"""
data=pd.read_excel(r'C:/Users\ASUS\Desktop\代码\美赛\C题\代码\4\positive one.xlsx')
time=data['Submission Date']
ti=[]
for i in range(13):
    ti.append((time[i+1]-time[i]).days)
print(ti)
"""
data=pd.read_excel(r'C:\Users\ASUS\Desktop\代码\美赛\C题\2021_MCM_Problem_C_Data\2021_MCM_Problem_C_Data\2021MCMProblemC_DataSet.xlsx')
data=data['Submission Date']
inter1=data.value_counts()
inter1.to_excel('5.xlsx')