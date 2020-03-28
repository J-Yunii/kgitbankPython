import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.read_csv('cine.csv',engine='python',encoding='utf-8')

print(df['movieNm'].head(20))
 
temp1 = df[df['movieNm'] == '드래곤 길들이기 3']

print(temp1)
mpl.rc('font', family='Malgun Gothic') #한글 폰트 설정
plt.plot([str(x) for x in temp1['targetDt']], temp1['salesAmt'])
plt.title('영화명 "블랙 팬서"의 일별 매출액(salesAmt) 선 그래프')
plt.xlabel('날짜')
plt.ylabel('매출액')
plt.xticks(fontsize=6, rotation=90)
plt.show()