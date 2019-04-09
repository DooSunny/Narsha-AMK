from pyowm import OWM
API_Key = '514fe4395b0b19b155eab8f4e4e150cc'
owm = OWM(API_Key)

where = owm.weather_at_place('Daegu')
getto = where.get_weather()

print('대구 : ', getto.get_status(), getto.get_temperature(unit='celsius')['temp'], '\'C')
#Using Open Weather Map api 

#공공데이터 API로 미세먼지 데이터 가져올 예정
#주소값을 받아와서 자동 지역설정 할 예정