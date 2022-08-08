import requests
import json
import time
import pandas as pd



api_key = "RGAPI-56cbca69-57d4-413b-b37f-a393980b0afe"
temp_puuid = "6GmLC8TVIQy5iXPOndeFSCQc-9tGH7LFGoN_Ryk9IOoWIuHmFE0W52V7CNNKLrpbIIt4yYdvIC7kBA"
match = 'https://asia.api.riotgames.com/lol/match/v5/matches/KR_6016635184/timeline?api_key=' + api_key
r = requests.get(match)#매치데이터 호출
league_df = pd.DataFrame(r.json())
league_df.info()
#aaa = r.json()
print(type(league_df['info']['frames'][1]['participantFrames']['1']['championStats']))
#print(league_df['info']['frames'][1])
print("  ")
#pd.DataFrame([league_df['info']['frames'][1]['participantFrames']['1']]).to_csv('temp.csv',index=False,encoding = 'cp949')
qqq = pd.DataFrame(league_df['info']['frames'][1]['participantFrames']['1'])

a1 = pd.DataFrame(league_df['info']['frames'][1]['participantFrames']['1']['championStats'])
a2 = pd.DataFrame(league_df['info']['frames'][1]['participantFrames']['1']['damageStats'])
qqq.drop(['championStats','damageStats'],axis = 1)
qqq = pd.concat([qqq,a1,a2], axis=1)
qqq.to_csv('temp2.csv',index=False,encoding = 'cp949')


                  
