import requests
import json
import time
import pandas as pd



api_key = "RGAPI-0cb315b9-0b8b-44b7-96e5-8687e479ff36"
temp_puuid = "6GmLC8TVIQy5iXPOndeFSCQc-9tGH7LFGoN_Ryk9IOoWIuHmFE0W52V7CNNKLrpbIIt4yYdvIC7kBA"
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
#pd.DataFrame([league_df['info']['frames'][1]['participantFrames']['1']]).to_csv('temp.csv',index=False,encoding = 'cp949')
for i in range(len(league_df['info']['frames'])):
    try:
        qqq = pd.DataFrame(league_df['info']['frames'][i]['participantFrames']['1'], index = [0])
        qqq = qqq.drop(['championStats','damageStats','position'],axis = 1)
        a1 = pd.DataFrame([league_df['info']['frames'][i]['participantFrames']['1']['championStats']])
        print(' a')
        a2 = pd.DataFrame([league_df['info']['frames'][i]['participantFrames']['1']['damageStats']])
        a3 = pd.DataFrame([league_df['info']['frames'][i]['participantFrames']['1']['position']])
        qqq = pd.concat([qqq,a1,a2, a3], axis=1)
        print(' b')
        data.loc[i] = qqq
        print(i,'/',len(league_df['info']['frames']))
    except:
        print(' error! = ' , i)
        
    
data.to_csv('temp2.csv',index=False,encoding = 'cp949')
#a1.to_csv('temp3.csv',index=False,encoding = 'cp949')


                  
