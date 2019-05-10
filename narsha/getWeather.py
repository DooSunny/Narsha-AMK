from datetime import datetime  #년, 월, 일, 시, 분, 초 등등 가져올 수 있는 라이브러리
import json #json 데이터를 가공할 수 있는 라이브러리
import requests

def getWeather(location):

    locationNX = '89'
    locationNY = '89'

    if(location == "서울"):
        locationNX = '60'
        locationNY = '127'
    elif(location == "대전"):
        locationNX = '67'
        locationNY = '100'
    elif(location == "세종"):
        locationNX = '66'
        locationNY = '103'
    elif(location == "광주"):
        locationNX = '58'
        locationNY = '74'
    elif(location == "울산"):
        locationNX = '102'
        locationNY = '84'
    elif(location == "대구"):
        locationNX = '89'
        locationNY = '90'
    elif(location == "부산"):
        locationNX = '98'
        locationNY = '76'
    elif(location == "제주"):
        locationNX = '52'
        locationNY = '38'

    transmitToAPI(locationNX, locationNY)

def transmitToAPI(NX, NY):

    shortTermForecastUrl = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib?"
    townForecastUrl = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?"
    service_Key = "serviceKey=" +"64QV0MQgjFD8HAnIKbqBycsrsYDMDELB1D3FZu6Nw3K7XVNkdflOhG%2Bm3wga8323saA7yX0K6HHD4HANv9i11w%3D%3D" +"&"
    date = "base_date=" +datetime.today().strftime("%Y%m%d") +"&" 
    type = "&_type=json"

    nx = "nx=" +NX
    ny = "&ny=" +NY

    restTemp = parse(townForecastUrl+service_Key+date+getUpdateTime1()+nx+ny+type)
    print ("오늘의 강수확률 : ", restTemp['response']['body']['items']['item'][0]['fcstValue'], "%")

    restTemp = parse(shortTermForecastUrl+service_Key+date+getUpdateTime2()+nx+ny+type)
    print("현재 온도 : ", restTemp['response']['body']['items']['item'][3]['obsrValue'], "˙C") 
    print("현재 습도 : ", restTemp['response']['body']['items']['item'][1]['obsrValue'], "%")
    
def parse(url):
    
    response = requests.get(url)
    getData = json.loads(response.text)
    return getData

def getUpdateTime1(): 

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

getWeather('대구')
#transmitToAPI('89', '89')
