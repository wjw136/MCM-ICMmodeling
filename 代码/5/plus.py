import pandas as pd
import numpy as np
import matplotlib as plt
data=pd.read_excel(r'C:\Users\ASUS\Desktop\代码\美赛\C题\代码\5\5.xlsx')
data=data['Submission number']
a=[]
for i in data:
    for j in range(i):
        a.append(1/i)
a=pd.Series(a)
a.to_excel('5+.xlsx')