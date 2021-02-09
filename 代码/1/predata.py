import numpy as np
import pandas as pd

from datetime import datetime
import matplotlib.pyplot as plt
#alld=pd.read_excel(r"C:\Users\ASUS\Desktop\代码\美赛\C题\2021_MCM_Problem_C_Data\2021_MCM_Problem_C_Data\2021MCMProblemC_DataSet.xlsx")
#posd=alld.loc[alld['Lab Status']=='Positive ID',:]
#px=posd.loc[:,'Latitude']
#py=posd.loc[:,'Longitude']
#pid=posd.loc[:,'GlobalID']
"""
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
area = np.pi * 4 ** 2  # 点面积
font2 = {'family' : 'SimHei',
'weight' : 'normal',
'size'   : 30,
}
plt.xlabel('latitude',font2)
plt.ylabel('longitude',font2)
plt.title('Asian Giant Hornet',font2)
plt.scatter(px, py, s=area, c='r', alpha=0.4)
plt.savefig('f1',bbox_inches = 'tight')
plt.show()


with open('HornetGlobalId.txt','a') as file_handle:   # .txt可以不自己新建,代码会自动新建
    for sinpid in pid:
        file_handle.write(str(sinpid))     # 写入
        file_handle.write('\n')         # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
"""
alld=pd.read_excel(r'C:\Users\ASUS\Desktop\代码\美赛\C题\代码\positive one.xlsx')
pla=alld.loc[:,'Latitude']
plo=alld.loc[:,'Longitude']
#print(pla)
x=[]
y=[]
for i in range(14):
    x.append((plo[i]+123.9431)/0.4)
    y.append((pla[i]-48.7775)/0.25)

alld['x']=x
alld['y']=y
alld.to_excel(r'C:\Users\ASUS\Desktop\代码\美赛\C题\代码\positive one.xlsx')