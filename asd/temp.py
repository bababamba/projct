import requests
import json
import time
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import warnings


data = pd.read_csv('매치데이터.csv')

data = data.dropna(axis=0)

print(data.shape[1])
for i in range(0,data.shape[1]):
    if i == 1 or i == 2 or i == 5 or i == 7 or i == 9 or i == 11:
        le = LabelEncoder()
        y = list(data.iloc[:,i])

        le.fit(y)
        y2 = le.transform(y)

        data.iloc[:,i] = y2
data2 = data[list(data.columns)[2:]]
print(data)
print(np.array(data['win'].tolist()))
data2.to_csv('temp3.csv',index=False,encoding = 'cp949')
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(data2, np.array(data['win'].tolist()), test_size=0.25, stratify=np.array(data['win'].tolist()), random_state=123456)


from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=12345)
rf.fit(X_train, y_train)

from sklearn.metrics import accuracy_score

predicted = rf.predict(X_test)
accuracy = accuracy_score(y_test, predicted)

#oob_score = out of bag score로써 예측이 얼마나 정확한가에 대한 추정치입니다.
print(f'Out-of-bag score estimate: {rf.oob_score_:.3}')
print(f'Mean accuracy score: {accuracy:.3}')
print(list(rf.feature_importances_))

from sklearn.ensemble import GradientBoostingClassifier
clf_gbc = GradientBoostingClassifier()
clf_gbc.fit(X_train,y_train)

y_pred = clf_gbc.predict(X_test)

print('테스트 정확도 = ' + str(accuracy_score(y_test,y_pred)))
print(list(clf_gbc.feature_importances_))

























'''
api_key = "RGAPI-27112419-0e70-4557-be7f-4522708f8e1d"
temp_puuid = "6GmLC8TVIQy5iXPOndeFSCQc-9tGH7LFGoN_Ryk9IOoWIuHmFE0W52V7CNNKLrpbIIt4yYdvIC7kBA"
match = 'https://asia.api.riotgames.com/lol/match/v5/matches/KR_6016635184/?api_key=' + api_key
r = requests.get(match)#매치데이터 호출
league_df = pd.DataFrame(r.json())
#league_df.info()
data = pd.DataFrame()
#aaa = r.json()
#print(league_df['info']['participants'])
#print(league_df['info']['teams'])


#qqq.to_csv('temp3.csv',index=False,encoding = 'cp949')

match = 'https://asia.api.riotgames.com/lol/match/v5/matches/KR_6016635184/timeline?api_key=' + api_key
r = requests.get(match)#매치데이터 호출
league_df = pd.DataFrame(r.json())
league_df.info()
data = pd.DataFrame()
#aaa = r.json()
print(type(league_df['info']['frames'][1]['participantFrames']['1']))

print(league_df['info']['frames'][1]['participantFrames']['1'])
print(league_df['info']['frames'][2]['participantFrames']['1'])
print(len(league_df['info']['frames']))
#print(league_df['info']['frames'][1])
print("  ")
a = '0'
#pd.DataFrame([league_df['info']['frames'][1]['participantFrames']['1']]).to_csv('temp.csv',index=False,encoding = 'cp949')
for i in range(1,11):
    try:
        for j in range(0,len(league_df['info']['frames'])):
            try:
                a = str(i)
                qqq = pd.DataFrame(league_df['info']['frames'][j]['participantFrames'][a], index = [0])
                qqq = qqq.drop(['championStats','damageStats','position'],axis = 1)
                a1 = pd.DataFrame([league_df['info']['frames'][j]['participantFrames'][a]['championStats']])
                a2 = pd.DataFrame([league_df['info']['frames'][j]['participantFrames'][a]['damageStats']])
                a3 = pd.DataFrame([league_df['info']['frames'][j]['participantFrames'][a]['position']])
                qqq = pd.concat([qqq,a1,a2, a3], axis=1)
                data = pd.concat([data,qqq])
                print(j+1,'/',len(league_df['info']['frames']),' , ',i,'/10')
            except:
                print(' jerror! = ' , j)
    except:
        print(' ierror! = ' , i)
        
    
data.to_csv('temp2.csv',index=False,encoding = 'cp949')
#a1.to_csv('temp3.csv',index=False,encoding = 'cp949')


                  
'''
