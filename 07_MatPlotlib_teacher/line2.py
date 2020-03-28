import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.read_csv(r'D:\토닥토닥파이썬\소스\데이터분석\데이터분석과제\kobis_boxoffice.csv',engine='python',encoding='cp949')

print(df.head(20))