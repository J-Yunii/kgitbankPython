import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rc('font', family='Malgun Gothic') #한글 폰트 설정
plt.plot(['A','B','C','D'],[1,2,3,4])
plt.title('선 그래프')
plt.xlabel('날짜')
plt.ylabel('매출액')
plt.show()