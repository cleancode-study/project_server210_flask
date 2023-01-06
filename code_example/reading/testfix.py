import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib

#---------------------------
# 연도 입력
year = '2011'
#---------------------------

font_manager.get_fontconfig_fonts()
# font_location = 'D:\\\\cleancode\\\\projectCovid19Server210\\\\code_example\\\\reading\\\\NaverNanumSquareNeo\\\\TTF\\\\NanumSquareNeo-aLt.ttf' # For Windows
font_location = 'C:/Windows/Fonts/Easop.ttf'
# font_name = font_manager.FontProperties(fname=font_location)
font_name = font_manager.FontProperties(fname=font_location).get_name()
# plt.title('예시 graph', fontproperties=font_name)
# matplotlib.rc('font', family=font_name)
# print(fm.get_font())

# path = os.path.abspath('reading books')
## 기존 csv는 컬럼명을 인식하지 못하여 년도 튜플을 삭제하고 컬럼제목 1개만 남긴 reading.csv 사용
# df = pd.read_csv('./data/종이책, 전자책, 오디오북 (성인)_encode.csv')
df = pd.read_csv('reading.csv')

## 튜플 중 특성별(1)의 값이 연령인 튜플만 조회
is_data = df[df['특성별(1)'] == '연령']
## 피처 '독서인구 1인당 평균독서권수 (권)_2011','인구 1인당 평균독서권수 (권)_2011' 개만 남김
is_data = is_data[['특성별(2)','독서인구 1인당 평균독서권수 (권)_'+year,'인구 1인당 평균독서권수 (권)_'+year]]
## NaN 결측치를 0으로 채움
is_data = is_data.fillna(0)

print(is_data)
## pyplot의 y축 값을 계속 추가하는 코드
matplotlib.rc('font',family=font_name)
# plt.title('예시 graph', fontproperties=font_name)
# plt.rc('font', family=font_name.get_name())        # 기본 폰트 크기
# rc('font', family=font_name.get_name())
plt.plot(is_data['특성별(2)'], is_data['독서인구 1인당 평균독서권수 (권)_'+year], color = 'red')
plt.plot(is_data['특성별(2)'], is_data['인구 1인당 평균독서권수 (권)_'+year], color = 'blue')

plt.show()