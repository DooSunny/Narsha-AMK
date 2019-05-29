#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example 1: GiGA Genie Keyword Spotting"""
import MicrophoneStream as MS
import ex1_Clock
import call_stt
import newspaperdaum as news
import ex1_getWeather as weather
# import newspaperdaum

def main():
	output_file = "testtts.wav"
	i=0
	while True :
		text=call_stt.Call()
		if "안녕" in text:
			call_stt.getText2VoiceStream("안녕하세요. 반갑습니다.", output_file)
		elif "이름" in text:
			call_stt.getText2VoiceStream("제 이름은 기가지니입니다.", output_file)

		elif ("몇시" in text) or ("시간" in text):
			hour=ex1_Clock.Clock_hour()
			minute=ex1_Clock.Clock_minute()
			call_stt.getText2VoiceStream("지금은 "+hour+"시, "+str(minute)+"분 입니다.", output_file)
		elif "뉴스" in text:
			for title in news.newspaperdaum.setarticle(news.newspaperdaum):
				call_stt.getText2VoiceStream(title,output_file)
				MS.play_file(output_file)
				for result in news.newspaperdaum.getnews(news.newspaperdaum):
					call_stt.getText2VoiceStream(result.text,output_file)
					MS.play_file(output_file)
					i+=1
					if i>2:
						print("\n")
						break 
		elif "날씨" in text:
			founded = False
			for local in weather.local_coords.keys():
				if local in text: 
					call_stt.getText2VoiceStream(create_weather_text(local), output_file)
					founded = True
					break
			if not founded: call_stt.getText2VoiceStream("현재는 특별시, 광역시, 자치도의 조회만 가능합니다", output_file)
								
		else:
			call_stt.getText2VoiceStream("알아들을 수 가 없습니다. 다시한번 말씀 해주세요.", output_file)

		MS.play_file(output_file)

def create_weather_text(local_name):
	weather_info = weather.get_weather_by_coord(weather.get_coords_by_local_name(local_name))
	if weather_info != None:
		return "현재 온도는 " + str(weather_info['main']['temp']) + "도이고, 습도는 " + str(weather_info['main']['humidity']) + "퍼센트입니다."
	else:
		return "날씨를 받아오던 중 오류가 발생하였습니다."

if __name__ == '__main__':
	main()