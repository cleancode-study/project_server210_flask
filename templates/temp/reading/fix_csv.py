import os
import pandas as pd

# path = os.path.abspath('reading books')
## 기존 csv는 컬럼명을 인식하지 못하여 년도 튜플을 삭제하고 컬럼제목 1개만 남긴 reading.csv 사용
# df = pd.read_csv('./data/종이책, 전자책, 오디오북 (성인)_encode.csv')
df = pd.read_csv('reading.csv')

## 튜플 중 특성별(1)의 값이 연령인 튜플만 조회
is_data = df[df['특성별(1)'] == 'age']
is_data = is_data.drop(labels='특성별(1)',axis=1)
# ## NaN 결측치를 0으로 채움
is_data = is_data.fillna(0)

# axis 변경
is_data = is_data.transpose()
# is_data = is_data.reset_index()
print(is_data)
is_data.to_csv('test.csv')



