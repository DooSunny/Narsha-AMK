from pyowm import OWM
API_Key = '514fe4395b0b19b155eab8f4e4e150cc'
owm = OWM(API_Key)

where = owm.weather_at_place('Daegu')
getto = where.get_weather()

print('deagu : ', getto.get_status(), getto.get_temperature(unit='celsius')['temp'])
#Using Open Weather Map api 