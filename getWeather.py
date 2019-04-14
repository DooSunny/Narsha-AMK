from pyowm import OWM

def getLocate():
    

def getWeater():
    API_Key = '514fe4395b0b19b155eab8f4e4e150cc'
    owm = OWM(API_Key)

    where = owm.weather_at_place('Daegu')
    getto = where.get_weather()

    print('대구 : ', getto.get_status(), getto.get_temperature(unit='celsius')['temp'], '\'C')

#Using Open Weather Map api 



#공공데이터 API로 미세먼지 데이터 가져올 예정
#주소값을 받아와서 자동 지역설정 할 예정

from datetime import datetime  #년, 월, 일, 시, 분, 초 등등 가져올 수 있는 라이브러리
import json #json 데이터를 가공할 수 있는 라이브러리
import requests

def getWeather2():

    url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?"
    service_Key = "serviceKey=" +"64QV0MQgjFD8HAnIKbqBycsrsYDMDELB1D3FZu6Nw3K7XVNkdflOhG%2Bm3wga8323saA7yX0K6HHD4HANv9i11w%3D%3D" +"&"

    date = "base_date=" +datetime.today().strftime("%Y%m%d") +"&" ## -> 2019년 4월 11일 일때 20190411 반환
    currentHour = datetime.today().hour;
    updatedTime = ""
    ##2, 5, 8, 11, 14, 17, 20, 23 -> 업데이트 타임
    if (2 <= currentHour and currentHour < 5):
        updatedTime = "02"
    if (5 <= currentHour and currentHour < 8):
        updatedTime = "05"
    if (8 <= currentHour and currentHour < 11):
        updatedTime = "08"
    if (11 <= currentHour and currentHour < 14):
        updatedTime = "11"
    if (14 <= currentHour and currentHour < 17):
        updatedTime = "14"      
    if (17 <= currentHour and currentHour < 20):
        updatedTime = "17"
    if (20 <= currentHour and currentHour < 23):
        updatedTime = "20"
    if (23 <= currentHour and currentHour <=24) or (0 <= currentHour and currentHour < 2) :
        updatedTime = "23"

    time = "base_time=" +updatedTime +"00&"

#위치는 stt연동시 하갔음 지금은 달성군
    locationNX = "nx=86&"
    locationNY = "ny=86&"
    type = "_type=json"

    rest = url+service_Key+date+time+locationNX+locationNY+type 
    parse(rest)

def parse(url):
    
    response = requests.get(url)
    getJson = json.loads(response.text)
    print(getJson)

    data = json.loads(getJson)

    print(data[""])


getWeather();

