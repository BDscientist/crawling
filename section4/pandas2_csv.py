import pandas as pd
import sys
import io
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
'''
#특정 문자 구분
df2 = pd.read_csv('c:/section4/csv_s2.csv',sep=';', skiprows=[0], header=None, names=["First name", "Test1", "Test2", "Test3", "Final", "Grade"])
df2['Grade'] = df2['Grade'].str.replace('"', ' ')
df2['Avg'] = df2[['Test1','Test2','Test3','Final']].mean(axis=1)
df2['Sum'] = df2[['Test1','Test2','Test3','Final']].sum(axis=1)

print(df2)

#CSV 쓰기
#df2.to_csv('c:/section4/result.csv')
df2.to_csv('c:/section4/result.csv',index=False)

'''

#랜덤으로 DataFrame 생성
df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
#df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))
print(df)

#CSV 쓰기
df.to_csv('c:/section4/result.csv',index=False)
#df.to_csv('c:/section4/result.csv',index=False,header=False)
