import requests

local_coords = {
    "서울": (37.55, 127),
    "대전": (36.33, 127.4),
    "세종": (36.51, 127.25),
    "광주": (35.14, 126.84),
    "울산": (35.54, 129.3),
    "대구": (35.86, 128.6),
    "부산": (35.16, 129.06),
    "제주": (33.5, 126.53)
}

def get_coords_by_local_name(local_name):
    if local_name in local_coords:
        return local_coords[local_name]
    else:
        return (89, 89)

def get_weather_by_coord(coord):
    lat = str(coord[0])
    lon = str(coord[1])

    app_id = "7e4ce0b05622c372120a3f66e79b5355"
    unit = "metric"
    current_weather_api_url = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid=" + app_id + "&units=" + unit

    result = request_get(current_weather_api_url)
    
    return result
    
def request_get(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    print(get_weather_by_coord(get_coords_by_local_name('대구')))