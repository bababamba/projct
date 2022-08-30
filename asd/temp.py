import requests
import json
import time
import pandas as pd
import numpy as np


api_key = "RGAPI-2aca8583-eec1-420d-937c-818fd5b2e357"
temp_puuid = "6GmLC8TVIQy5iXPOndeFSCQc-9tGH7LFGoN_Ryk9IOoWIuHmFE0W52V7CNNKLrpbIIt4yYdvIC7kBA"
match = 'https://asia.api.riotgames.com/lol/match/v5/matches/KR_6092506289/?api_key=' + api_key
r = requests.get(match)#매치데이터 호출
league_df = pd.DataFrame(r.json())
data1 = pd.DataFrame()
data2 = pd.DataFrame()
data3 = pd.DataFrame()
data4 = pd.DataFrame()
data5 = pd.DataFrame()

 
#league_df.info()
for j in range(0,5) :
    qq1 = pd.DataFrame(league_df['info']['participants'][j])
    qq2 = pd.DataFrame(league_df['info']['participants'][j+5])
    
    if j==0:
        temp1 =pd.DataFrame(pd.Series({"tT1Win":qq1['win'].iloc[0],"T1DealtDamage":qq1['totalDamageDealtToChampions'].iloc[0],"T1TakenDamage":qq1['totalDamageTaken'].iloc[0],"T1VisionScore":qq1['visionScore'].iloc[0],"T1champLevel":qq1['champLevel'].iloc[0],"T1goldEarned":qq1['goldEarned'].iloc[0],"T1totalMinionsKilled":qq1['totalMinionsKilled'].iloc[0]})).T
        temp2 =pd.DataFrame(pd.Series({"tT2Win":qq2['win'].iloc[0],"T2DealtDamage":qq2['totalDamageDealtToChampions'].iloc[0],"T2TakenDamage":qq2['totalDamageTaken'].iloc[0],"T2VisionScore":qq2['visionScore'].iloc[0],"T2champLevel":qq2['champLevel'].iloc[0],"T2goldEarned":qq2['goldEarned'].iloc[0],"T2totalMinionsKilled":qq2['totalMinionsKilled'].iloc[0]})).T
        temp1 = pd.concat([temp1,temp2], axis=1)
        data1 = pd.concat([data1,temp1], axis=0)
    elif j==1:
        temp1 =pd.DataFrame(pd.Series({"jT1Win":qq1['win'].iloc[0],"T1DealtDamage":qq1['totalDamageDealtToChampions'].iloc[0],"T1TakenDamage":qq1['totalDamageTaken'].iloc[0],"T1VisionScore":qq1['visionScore'].iloc[0],"T1champLevel":qq1['champLevel'].iloc[0],"T1goldEarned":qq1['goldEarned'].iloc[0],"T1totalMinionsKilled":qq1['totalMinionsKilled'].iloc[0]})).T
        temp2 =pd.DataFrame(pd.Series({"jT2Win":qq2['win'].iloc[0],"T2DealtDamage":qq2['totalDamageDealtToChampions'].iloc[0],"T2TakenDamage":qq2['totalDamageTaken'].iloc[0],"T2VisionScore":qq2['visionScore'].iloc[0],"T2champLevel":qq2['champLevel'].iloc[0],"T2goldEarned":qq2['goldEarned'].iloc[0],"T2totalMinionsKilled":qq2['totalMinionsKilled'].iloc[0]})).T
        temp1 = pd.concat([temp1,temp2], axis=1)
        data2 = pd.concat([data2,temp1], axis=0)
    elif j==2:
        temp1 =pd.DataFrame(pd.Series({"mT1Win":qq1['win'].iloc[0],"T1DealtDamage":qq1['totalDamageDealtToChampions'].iloc[0],"T1TakenDamage":qq1['totalDamageTaken'].iloc[0],"T1VisionScore":qq1['visionScore'].iloc[0],"T1champLevel":qq1['champLevel'].iloc[0],"T1goldEarned":qq1['goldEarned'].iloc[0],"T1totalMinionsKilled":qq1['totalMinionsKilled'].iloc[0]})).T
        temp2 =pd.DataFrame(pd.Series({"mT2Win":qq2['win'].iloc[0],"T2DealtDamage":qq2['totalDamageDealtToChampions'].iloc[0],"T2TakenDamage":qq2['totalDamageTaken'].iloc[0],"T2VisionScore":qq2['visionScore'].iloc[0],"T2champLevel":qq2['champLevel'].iloc[0],"T2goldEarned":qq2['goldEarned'].iloc[0],"T2totalMinionsKilled":qq2['totalMinionsKilled'].iloc[0]})).T
        temp1 = pd.concat([temp1,temp2], axis=1)
        data3 = pd.concat([data3,temp1], axis=0)
    elif j==3:
        temp1 =pd.DataFrame(pd.Series({"aT1Win":qq1['win'].iloc[0],"T1DealtDamage":qq1['totalDamageDealtToChampions'].iloc[0],"T1TakenDamage":qq1['totalDamageTaken'].iloc[0],"T1VisionScore":qq1['visionScore'].iloc[0],"T1champLevel":qq1['champLevel'].iloc[0],"T1goldEarned":qq1['goldEarned'].iloc[0],"T1totalMinionsKilled":qq1['totalMinionsKilled'].iloc[0]})).T
        temp2 =pd.DataFrame(pd.Series({"aT2Win":qq2['win'].iloc[0],"T2DealtDamage":qq2['totalDamageDealtToChampions'].iloc[0],"T2TakenDamage":qq2['totalDamageTaken'].iloc[0],"T2VisionScore":qq2['visionScore'].iloc[0],"T2champLevel":qq2['champLevel'].iloc[0],"T2goldEarned":qq2['goldEarned'].iloc[0],"T2totalMinionsKilled":qq2['totalMinionsKilled'].iloc[0]})).T
        temp1 = pd.concat([temp1,temp2], axis=1)
        data4 = pd.concat([data4,temp1], axis=0)
    elif j==4:
        temp1 =pd.DataFrame(pd.Series({"sT1Win":qq1['win'].iloc[0],"T1DealtDamage":qq1['totalDamageDealtToChampions'].iloc[0],"T1TakenDamage":qq1['totalDamageTaken'].iloc[0],"T1VisionScore":qq1['visionScore'].iloc[0],"T1champLevel":qq1['champLevel'].iloc[0],"T1goldEarned":qq1['goldEarned'].iloc[0],"T1totalMinionsKilled":qq1['totalMinionsKilled'].iloc[0]})).T
        temp2 =pd.DataFrame(pd.Series({"sT2Win":qq2['win'].iloc[0],"T2DealtDamage":qq2['totalDamageDealtToChampions'].iloc[0],"T2TakenDamage":qq2['totalDamageTaken'].iloc[0],"T2VisionScore":qq2['visionScore'].iloc[0],"T2champLevel":qq2['champLevel'].iloc[0],"T2goldEarned":qq2['goldEarned'].iloc[0],"T2totalMinionsKilled":qq2['totalMinionsKilled'].iloc[0]})).T
        temp1 = pd.concat([temp1,temp2], axis=1)
        data5 = pd.concat([data5,temp1], axis=0)
   

print(data1)
print(data2)
print(data3)
print(data4)
print(data5)
#qqq = qqq.drop(['doubleKills','tripleKills','quadraKills','baronKills', 'basicPings','lane', 'bountyLevel', 'challenges','championId', 'championName', 'championTransform', 'consumablesPurchased','eligibleForProgression', 'gameEndedInEarlySurrender', 'gameEndedInSurrender','individualPosition','item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'itemsPurchased', 'largestCriticalStrike','nexusKills', 'nexusLost', 'nexusTakedowns','participantId','perks','profileIcon', 'puuid','riotIdName', 'riotIdTagline', 'role', 'spell1Casts', 'spell2Casts', 'spell3Casts', 'spell4Casts', 'summoner1Casts', 'summoner1Id', 'summoner2Casts', 'summoner2Id', 'summonerId', 'summonerLevel', 'summonerName', 'teamEarlySurrendered', 'teamId', 'teamPosition', 'timePlayed', 'turretTakedowns','win'],axis = 1)
#qqq = qqq.drop(['baronKills', 'basicPings','lane', 'bountyLevel', 'challenges','championId', 'championName', 'championTransform', 'consumablesPurchased','eligibleForProgression', 'gameEndedInEarlySurrender', 'gameEndedInSurrender','individualPosition','item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'itemsPurchased', 'largestCriticalStrike','nexusKills', 'nexusLost', 'nexusTakedowns','participantId','perks','profileIcon', 'puuid','riotIdName', 'riotIdTagline', 'role', 'spell1Casts', 'spell2Casts', 'spell3Casts', 'spell4Casts', 'summoner1Casts', 'summoner1Id', 'summoner2Casts', 'summoner2Id', 'summonerId', 'summonerLevel', 'summonerName', 'teamEarlySurrendered', 'teamId', 'teamPosition', 'timePlayed', 'turretTakedowns','win'],axis = 1)
#www = qqq.pop('assists','champLevel','deaths','detectorWardsPlaced','goldEarned','kills','totalDamageDealt', 'wardsKilled', 'wardsPlaced')
#www = qqq.pop('assists','kills','deaths')
#aaa = r.json()


#print(league_df['info']['teams'])


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
