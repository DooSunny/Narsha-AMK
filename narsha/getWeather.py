from datetime import datetime  #년, 월, 일, 시, 분, 초 등등 가져올 수 있는 라이브러리
import json #json 데이터를 가공할 수 있는 라이브러리
import requests
#위치는 stt연동시 하갔음 지금은 달성군
locationNX = "nx=86&"
locationNY = "ny=86&"

# def voice():

#     if(v == "deagu"):
#         locationNX = "nx=86&"
#         locationNY = "ny=86&"
#     if(v == "sad"):
#         locationNX = "nx=86&"
#         locationNY = "ny=86&"

def getWeather2():

    초단기실황url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib?"
    초단기예보url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData?"
    동네예보url =   "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?"
    service_Key = "serviceKey=" +"64QV0MQgjFD8HAnIKbqBycsrsYDMDELB1D3FZu6Nw3K7XVNkdflOhG%2Bm3wga8323saA7yX0K6HHD4HANv9i11w%3D%3D" +"&"
    date = "base_date=" +datetime.today().strftime("%Y%m%d") +"&" ## -> 2019년 4월 11일 일때 20190411 반환

    type = "_type=json"

    rest1 = 동네예보url+service_Key+date+getUpdateTime1()+locationNX+locationNY+type 
    a = parse(rest1)
    # if(a['category'] == 'POP')
    #     print (a['fcstValue'])
    print (a)
    print("\n")
    rest2 = 초단기실황url+service_Key+date+getUpdateTime2()+locationNX+locationNY+type 
    b = parse(rest2)
    print(b)
    print("\n")
    rest3 = 초단기예보url+service_Key+date+getUpdateTime2()+locationNX+locationNY+type 
    c = parse(rest3)
    print(c)

def parse(url):
    
    response = requests.get(url)
    getJson = json.loads(response.text)
    #print(getJson)
    return getJson

def getUpdateTime1(): #동네예보 api 업데이트 타임

    currentHour = datetime.today().hour
    updateTime = ""
    ##2, 5, 8, 11, 14, 17, 20, 23 -> 업데이트 타임
    if (2 <= currentHour and currentHour < 5):
        updateTime = "02"
    if (5 <= currentHour and currentHour < 8):
        updateTime = "05"
    if (8 <= currentHour and currentHour < 11):
        updateTime = "08"
    if (11 <= currentHour and currentHour < 14):
        updateTime = "11"
    if (14 <= currentHour and currentHour < 17):
        updateTime = "14"      
    if (17 <= currentHour and currentHour < 20):
        updateTime = "17"
    if (20 <= currentHour and currentHour < 23):
        updateTime = "20"
    if (23 <= currentHour and currentHour <=24) or (0 <= currentHour and currentHour < 2) :
        updateTime = "23"

    return "base_time=" +str(updateTime) +"00&"

def getUpdateTime2():

    currentHour = datetime.today().hour
    currentMinute = datetime.today().minute

    if(0 <= currentMinute and currentMinute < 30):
        currentHour -= 1;
    
    return "base_time=" +str(currentHour) +"30&"
# def toString():
#     sadasd

getWeather2()

