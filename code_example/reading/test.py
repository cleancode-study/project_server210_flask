import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path = os.path.abspath('reading books')
## 기존 csv는 컬럼명을 인식하지 못하여 년도 튜플을 삭제하고 컬럼제목 1개만 남긴 reading.csv 사용
# df = pd.read_csv('./data/종이책, 전자책, 오디오북 (성인)_encode.csv')
df = pd.read_csv('reading.csv')

## 튜플 중 특성별(1)의 값이 연령인 튜플만 조회
is_data = df[df['특성별(1)'] == '연령']
## 피처 '독서인구 1인당 평균독서권수 (권)_2011','인구 1인당 평균독서권수 (권)_2011' 개만 남김
is_data = is_data[['특성별(2)','독서인구 1인당 평균독서권수 (권)_2011','인구 1인당 평균독서권수 (권)_2011']]
## NaN 결측치를 0으로 채움
is_data = is_data.fillna(0)
## 숫자로 컬럼을 인식하기 위해서 13~19세를 1319로 변경
is_data['특성별(2)'] = [1319, 1519, 2029, 3039, 4049, 5059, 6069, 7079, 8000]
print(is_data)
## pyplot의 y축 값을 계속 추가하는 코드
plt.plot(is_data[['특성별(2)']], is_data[['독서인구 1인당 평균독서권수 (권)_2011']], color = 'red')
plt.plot(is_data[['특성별(2)']], is_data[['인구 1인당 평균독서권수 (권)_2011']], color = 'blue')
# flg=plt.figure()
# ax = flg.add_subplot(111)
# ax.plot(df.index, df[df['13~19세']], label='13~19세')

# ax.plot(df.index, df['13~19세'], label='13~19세')
#
# ax.plot(df.index, df[df['13~19세']], label='13~19세')
# ax.plot(df.index, df['15~19세'], label='15~19세')
# ax.plot(df.index, df['20~29세'], label='20~29세')
# ax.plot(df.index, df['30~39세'], label='30~39세')
#
# ax.plot(df.index, df['40~49세'], label='40~49세')
# ax.plot(df.index, df['50~59세'], label='50~59세')
# ax.plot(df.index, df['60~69세'], label='60~69세')
# ax.plot(df.index, df['70~79세'], label='70~79세')
#
# ax.plot(df.index, df['80세 이상'], label='80세 이상')
#
# ax.set_title('연령별 독서량')
# ax.set_ylabel('연령대')
# ax.set_xlabel('년도')
#
# ax.legend()
plt.show()