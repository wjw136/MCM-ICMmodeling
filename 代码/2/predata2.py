import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
predata=pd.read_excel(r'C:\Users\ASUS\Desktop\代码\美赛\C题\代码\2\SVM final.xlsx')
predata=predata[predata['Lab Status']==True]
predata.to_excel(r'C:\Users\ASUS\Desktop\代码\美赛\C题\代码\2\positive one.xlsx')