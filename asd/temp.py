import requests
import json
import time
import pandas as pd
import numpy as np


api_key = "RGAPI-f31dcbe0-1111-4df9-b4d3-3c03cb30acda"
temp_puuid = "6GmLC8TVIQy5iXPOndeFSCQc-9tGH7LFGoN_Ryk9IOoWIuHmFE0W52V7CNNKLrpbIIt4yYdvIC7kBA"

  








































'''
match = 'https://asia.api.riotgames.com/lol/match/v5/matches/KR_6092506289/?api_key=' + api_key
r = requests.get(match)#매치데이터 호출
league_df = pd.DataFrame(r.json())
data1 = pd.DataFrame()
data2 = pd.DataFrame()
 
#league_df.info()
for j in range(0,5) :
    time = league_df['info']['gameDuration']
    time = round(time/60)
    kills1 = league_df['info']['teams'][0]['objectives']['champion']['kills']
    kills2= league_df['info']['teams'][1]['objectives']['champion']['kills']
    qq1 = pd.DataFrame(league_df['info']['participants'][j])
    qq2 = pd.DataFrame(league_df['info']['participants'][j+5])
    
    if j==0:
        a1 = qq1['totalDamageDealtToChampions'].iloc[0] +qq1['totalDamageTaken'].iloc[0]
        a1 = round(a1/time)
        a2 = qq2['totalDamageDealtToChampions'].iloc[0] +qq2['totalDamageTaken'].iloc[0]
        a2 = round(a2/time)
        data1 =pd.DataFrame(pd.Series({"T1TOP":a1})).T
        data2 =pd.DataFrame(pd.Series({"T2TOP":a2})).T
    elif j==1:
        a1 = qq1['kills'].iloc[0] + qq1['assists'].iloc[0]
        a1 = a1/kills1
        a2 = qq2['kills'].iloc[0] + qq2['assists'].iloc[0]
        a2 = a2/kills2
        temp1 =pd.DataFrame(pd.Series({"T1JUN":round(a1*100)})).T
        temp2 =pd.DataFrame(pd.Series({"T2JUN":round(a2*100)})).T
        data1 = pd.concat([data1,temp1], axis = 1)
        data2 = pd.concat([data2,temp2], axis = 1)
    elif j==2:
        a1 = round(qq1['totalDamageDealtToChampions'].iloc[0]/time)
        a2 = round(qq2['totalDamageDealtToChampions'].iloc[0]/time)
        temp1 =pd.DataFrame(pd.Series({"T1MID":a1})).T
        temp2 =pd.DataFrame(pd.Series({"T2MID":a2})).T
        data1 = pd.concat([data1,temp1], axis = 1)
        data2 = pd.concat([data2,temp2], axis = 1)
    elif j==3:
        a1 = round(qq1['totalDamageDealtToChampions'].iloc[0]/time)
        a2 = round(qq2['totalDamageDealtToChampions'].iloc[0]/time)
        temp1 =pd.DataFrame(pd.Series({"T1ADC":a1})).T
        temp2 =pd.DataFrame(pd.Series({"T2ADC":a2})).T
        data1 = pd.concat([data1,temp1], axis = 1)
        data2 = pd.concat([data2,temp2], axis = 1)
    elif j==4:
        temp1 =pd.DataFrame(pd.Series({"T1SPT":qq1['assists'].iloc[0]})).T
        temp2 =pd.DataFrame(pd.Series({"T2SPT":qq2['assists'].iloc[0]})).T
        data1 = pd.concat([data1,temp1], axis = 1)
        data2 = pd.concat([data2,temp2], axis = 1)
   
data1 = pd.concat([data1,data2], axis = 1)
print(data1)
#qqq = qqq.drop(['doubleKills','tripleKills','quadraKills','baronKills', 'basicPings','lane', 'bountyLevel', 'challenges','championId', 'championName', 'championTransform', 'consumablesPurchased','eligibleForProgression', 'gameEndedInEarlySurrender', 'gameEndedInSurrender','individualPosition','item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'itemsPurchased', 'largestCriticalStrike','nexusKills', 'nexusLost', 'nexusTakedowns','participantId','perks','profileIcon', 'puuid','riotIdName', 'riotIdTagline', 'role', 'spell1Casts', 'spell2Casts', 'spell3Casts', 'spell4Casts', 'summoner1Casts', 'summoner1Id', 'summoner2Casts', 'summoner2Id', 'summonerId', 'summonerLevel', 'summonerName', 'teamEarlySurrendered', 'teamId', 'teamPosition', 'timePlayed', 'turretTakedowns','win'],axis = 1)
#qqq = qqq.drop(['baronKills', 'basicPings','lane', 'bountyLevel', 'challenges','championId', 'championName', 'championTransform', 'consumablesPurchased','eligibleForProgression', 'gameEndedInEarlySurrender', 'gameEndedInSurrender','individualPosition','item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'itemsPurchased', 'largestCriticalStrike','nexusKills', 'nexusLost', 'nexusTakedowns','participantId','perks','profileIcon', 'puuid','riotIdName', 'riotIdTagline', 'role', 'spell1Casts', 'spell2Casts', 'spell3Casts', 'spell4Casts', 'summoner1Casts', 'summoner1Id', 'summoner2Casts', 'summoner2Id', 'summonerId', 'summonerLevel', 'summonerName', 'teamEarlySurrendered', 'teamId', 'teamPosition', 'timePlayed', 'turretTakedowns','win'],axis = 1)
#www = qqq.pop('assists','champLevel','deaths','detectorWardsPlaced','goldEarned','kills','totalDamageDealt', 'wardsKilled', 'wardsPlaced')
#www = qqq.pop('assists','kills','deaths')
#aaa = r.json()


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
