import requests
import json
import time
import pandas as pd



api_key = "RGAPI-d0186bd9-0bd0-42d2-ad96-e8506d357a60"
temp_puuid = "6GmLC8TVIQy5iXPOndeFSCQc-9tGH7LFGoN_Ryk9IOoWIuHmFE0W52V7CNNKLrpbIIt4yYdvIC7kBA"
match = 'https://asia.api.riotgames.com/lol/match/v5/matches/KR_6016635184/?api_key=' + api_key
r = requests.get(match)#매치데이터 호출
league_df = pd.DataFrame(r.json())
#league_df.info()
data = pd.DataFrame()
#aaa = r.json()
#print(league_df['info']['participants'])
print(league_df['info']['teams'])
qqq = pd.DataFrame(league_df['info']['teams'])

qqq = qqq.drop(['bans','objectives'],axis = 1)
print(qqq)
q1 = pd.DataFrame(qqq[0],index = [0])
www = pd.DataFrame(pd.Series({"BaronFirstKill":league_df['info']['teams'][0]['objectives']['baron']['first'], "BaronKills":league_df['info']['teams'][0]['objectives']['baron']['kills']})).T
qqq = qqq.pop('bans')
qqq = pd.concat([qqq,www],axis = 1)
print(qqq)
#qqq.to_csv('temp3.csv',index=False,encoding = 'cp949')
'''
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
