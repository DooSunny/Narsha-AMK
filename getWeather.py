from pyowm import OWM

API_Key = '514fe4395b0b19b155eab8f4e4e150cc'
owm = OWM(API_Key)

where = owm.weather_at_place('Daegu')
getto = where.get_weather()

print('대구 : ', getto.get_status(), getto.get_temperature(unit='celsius')['temp'], '\'C')
#Using Open Weather Map api 

#공공데이터 API로 미세먼지 데이터 가져올 예정
#주소값을 받아와서 자동 지역설정 할 예정
from datetime import datetime  #년, 월, 일, 시, 분, 초 등등 가져올 수 있는 라이브러리

Url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?"
         #서비스키&base_date=20151201&base_time=0600&nx=55&ny=127&pageNo=1&numOfRows=1&_type=json
Service_key = "serviceKey=" +"64QV0MQgjFD8HAnIKbqBycsrsYDMDELB1D3FZu6Nw3K7XVNkdflOhG%2Bm3wga8323saA7yX0K6HHD4HANv9i11w%3D%3D" +"&";

Date = "base_date=" +datetime.today().strftime("%Y%m%d") +"&"
 ## -> 2019년 4월 11일 일때 20190411 반환
tempTime = ""#정시로 마추기
##Time = "base_time=" +tempTime +"&"
##2, 5, 8, 11, 14, 17, 20, 23 -> 업데이트 타임
Time = "base_time=0500&"


#위치는 stt연동시 하갔음 지금은 달성군
LocationNX = "nx=86&"
LocationNY = "ny=86"

print(Url+Service_key+Date+Time+LocationNX+LocationNY) # rest 작동 확인




