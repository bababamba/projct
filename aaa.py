import requests
import json
import time
import pandas as pd



api_key = "RGAPI-0cb315b9-0b8b-44b7-96e5-8687e479ff36"
temp_puuid = "6GmLC8TVIQy5iXPOndeFSCQc-9tGH7LFGoN_Ryk9IOoWIuHmFE0W52V7CNNKLrpbIIt4yYdvIC7kBA"
grandmaster = 'https://kr.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=' + api_key
r = requests.get(grandmaster)#챌 데이터 호출
league_df = pd.DataFrame(r.json())
league_df.reset_index(inplace=True)#수집한 챌 index정리
league_entries_df = pd.DataFrame(dict(league_df['entries'])).T #list구조로 되어 있는 entries컬럼 풀어주기
league_df = pd.concat([league_df, league_entries_df], axis=1) #열끼리 결합
league_df = league_df.drop(['index', 'queue', 'name', 'leagueId', 'entries', 'rank'], axis=1)
league_df['puuid'] = ""
league_df.info()
league_df.to_csv('챌린데이터.csv',index=False,encoding = 'cp949')#중간저장
for i in range(2):
    try:
        
        time.sleep(1)
        sohwan = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + league_df['summonerName'].iloc[i] + '?api_key=' + api_key 
        r = requests.get(sohwan)
        while r.status_code == 429:
            print("라이엇때문이야!")
            time.sleep(5)
            sohwan = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + league_df['summonerName'].iloc[i] + '?api_key=' + api_key 
            r = requests.get(sohwan)
            
        puuid = r.json()['puuid']
        league_df.iloc[i, -1] = puuid
        print("1 - 1번 작업", i+1, "/", len(league_df))
    
    except:
        pass
league_df.to_csv('챌린데이터.csv',index=False,encoding = 'cp949')#저장

match_info_df = pd.DataFrame()
match_info_df.insert(0,'matchId',"")
start = str('0')
count = str('20')
for i in range(2):
    try:
        time.sleep(2)
        match0 = 'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/' + league_df.iloc[i,-1]  +'/ids?start=' + start + '&count=' + count + '&api_key=' + api_key
        r = requests.get(match0)
        
        while r.status_code == 429:
            print("라이엇때문이야!")
            time.sleep(5)
            match0 = 'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/' + league_df.iloc[i,-1]  +'/ids?start=' + start + '&count=' + count +'&api_key=' + api_key
        r = requests.get(match0)
        match_info_df = pd.concat([match_info_df, pd.DataFrame(r.json())])
        print("1 - 2번 작업", i+1, "/", len(league_df))
    
    except:
        print(i+1)
match_info_df.to_csv('매치리스트.csv',index=False,encoding = 'cp949')#저장      
#------------------------2번---------------------------------------------------

match_fin = pd.DataFrame()
for i in range(len(match_info_df)):    
    time.sleep(1)
    api_url='https://asia.api.riotgames.com/lol/match/v5/matches/' + str(match_info_df.iloc[i,0]) + '?api_key=' + api_key
    r = requests.get(api_url)

    if r.status_code == 200: # response가 정상이면 바로 맨 밑으로 이동하여 정상적으로 코드 실행
        pass

    elif r.status_code == 429:
        print('api cost full : infinite loop start')
        print('loop location : ',i)
        start_time = time.time()

        while True: # 429error가 끝날 때까지 무한 루프
            if r.status_code == 429:

                print('try 10 second wait time')
                time.sleep(10)

                r = requests.get(api_url)
                print(r.status_code)

            elif r.status_code == 200: #다시 response 200이면 loop escape
                print('total wait time : ', time.time() - start_time)
                print('recovery api cost')
                break

    elif r.status_code == 503: # 잠시 서비스를 이용하지 못하는 에러
        print('service available error')
        start_time = time.time()

        while True:
            if r.status_code == 503 or r.status_code == 429:

                print('try 10 second wait time')
                time.sleep(10)

                r = requests.get(api_url)
                print(r.status_code)

            elif r.status_code == 200: # 똑같이 response가 정상이면 loop escape
                print('total error wait time : ', time.time() - start_time)
                print('recovery api cost')
                break
    elif r.status_code == 403: # api갱신이 필요
        print('you need api renewal')
        print('break')
        break
    else:
        print('오류 발생! 오류코드:',r.status_code)
    # 위의 예외처리 코드를 거쳐서 내려왔을 때 해당 코드가 실행될 수 있도록 작성
    temp = r.json()
    mat = pd.DataFrame(list(temp['info'].values()), index=list(temp['info'].keys())).T
    match_fin = pd.concat([match_fin,mat])
    print('2번 작업',i+1,'/',len(match_info_df))

    
    #챔피언아이디를 제외하고 딕셔너리를 뽑는다
    a_ls = list(temp['info']['participants'])
    #team1
    team1_df = pd.DataFrame()
    for i in range(len(a_ls)):
        try:
            team1 = pd.DataFrame(list(a_ls[i].values()),index = list(a_ls[i].keys())).T
            team1_df = team1_df.append(team1)
        except:
            pass
        
    team1_df.index = range(len(team1_df))



    #컬럼으로 풀어준 team1과 team2와 duration의 데이터를 합쳐준다.
    data_team = pd.concat([team1_df,team2_df],axis=1)
    

match_fin.to_csv('매치데이터.csv',index=False,encoding = 'cp949')#저장
data_team.to_csv('매치데이터2.csv',index=False,encoding = 'cp949')#중간저장
# --------------3번-------------------------------------------


match_fin2 = pd.DataFrame()
for i in range(len(match_info_df)):    
    time.sleep(1)
    api_url='https://asia.api.riotgames.com/lol/match/v5/matches/' + str(match_info_df.iloc[i,0]) + '/timeline?api_key=' + api_key
    r = requests.get(api_url)

    if r.status_code == 200: # response가 정상이면 바로 맨 밑으로 이동하여 정상적으로 코드 실행
        pass

    elif r.status_code == 429:
        print('api cost full : infinite loop start')
        print('loop location : ',i)
        start_time = time.time()

        while True: # 429error가 끝날 때까지 무한 루프
            if r.status_code == 429:

                print('try 10 second wait time')
                time.sleep(10)

                r = requests.get(api_url)
                print(r.status_code)

            elif r.status_code == 200: #다시 response 200이면 loop escape
                print('total wait time : ', time.time() - start_time)
                print('recovery api cost')
                break

    elif r.status_code == 503: # 잠시 서비스를 이용하지 못하는 에러
        print('service available error')
        start_time = time.time()

        while True:
            if r.status_code == 503 or r.status_code == 429:

                print('try 10 second wait time')
                time.sleep(10)

                r = requests.get(api_url)
                print(r.status_code)

            elif r.status_code == 200: # 똑같이 response가 정상이면 loop escape
                print('total error wait time : ', time.time() - start_time)
                print('recovery api cost')
                break
    elif r.status_code == 403: # api갱신이 필요
        print('you need api renewal')
        print('break')
        break
    else:
        print('오류 발생! 오류코드:',r.status_code)
    # 위의 예외처리 코드를 거쳐서 내려왔을 때 해당 코드가 실행될 수 있도록 작성
    temp = r.json()
    mat = pd.DataFrame(list(temp.values()), index=list(temp.keys())).T
    match_fin2 = pd.concat([match_fin2,mat])
    print('3번 작업',i+1,'/',len(match_info_df))
    

match_fin2.to_csv('매치탐라데이터.csv',index=False,encoding = 'cp949')#저장

