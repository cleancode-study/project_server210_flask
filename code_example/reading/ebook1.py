import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path = os.path.abspath('reading books')
df = pd.read_csv(path+'/刀辑樊_1.csv', index_col=0, parse_dates=['Date'])
df

flg=plt.figure(flgsize=(20,8))
ax = flg.add_subplot(111)

ax.plot(df.index, df['13~19技'], label='13~19技')
ax.plot(df.index, df['15~19技'], label='15~19技')
ax.plot(df.index, df['20~29技'], label='20~29技')
ax.plot(df.index, df['30~39技'], label='30~39技')

ax.plot(df.index, df['40~49技'], label='40~49技')
ax.plot(df.index, df['50~59技'], label='50~59技')
ax.plot(df.index, df['60~69技'], label='60~69技')
ax.plot(df.index, df['70~79技'], label='70~79技')

ax.plot(df.index, df['80技 捞惑'], label='80技 捞惑')

ax.set_title('楷飞喊 刀辑樊')
ax.set_ylabel('楷飞措')
ax.set_xlabel('斥档')

ax.legend()
plt.show()