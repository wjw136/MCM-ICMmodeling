import numpy as np
import cv2
import os
import pandas as pd
import cv2
import numpy as np
fdata=pd.read_excel(r"C:/Users/ASUS/Desktop/代码/美赛/C题/代码/2'/ffdata.xlsx")
fdata1=fdata[fdata['Lab Status']==1]
fdata1.to_excel('ffdata(test).xlsx')