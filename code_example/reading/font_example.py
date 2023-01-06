#한글 폰트 사용
from matplotlib import font_manager,rc
import matplotlib
import matplotlib.pyplot as plt

#폰트 경로
# font_path = "C:/Windows/Fonts/H2GTRM.TTF"
font_path = 'C:/Windows/Fonts/Easop.ttf'

#폰트 이름 얻어오기
font_name = font_manager.FontProperties(fname=font_path).get_name()

#font 설정
matplotlib.rc('font',family=font_name)

#작업
plt.plot([1,2,3,4])
plt.xlabel("시간")
plt.ylabel("거리")
plt.show()