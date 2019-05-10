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
		if("안녕" in text):
			call_stt.getText2VoiceStream("안녕하세요. 반갑습니다.", output_file)
		elif("이름" in text):
			call_stt.getText2VoiceStream("제 이름은 기가지니입니다.", output_file)

		elif(("몇시" in text) or ("시간" in text) ):
			hour=ex1_Clock.Clock_hour()
			minute=ex1_Clock.Clock_minute()
			call_stt.getText2VoiceStream("지금은 "+hour+"시, "+str(minute)+"분 입니다.", output_file)
		elif("뉴스" in text):
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
		elif("날씨" in text):
			if("서울" in text): weather.getWeather("서울")
			elif("대전" in text): weather.getWeather("대전")
			elif("세종" in text): weather.getWeather("세종")
			elif("광주" in text): weather.getWeather("광주")
			elif("대구" in text): weather.getWeather("대구")
			elif("울산" in text): weather.getWeather("울산")
			elif("부산" in text): weather.getWeather("부산")
			elif("제주" in text): weather.getWeather("제주")		
			else: call_stt.getText2VoiceStream("현재는 특별시 광역시 자치도의 조회만 가능합니다", output_file)
								
		else:
			call_stt.getText2VoiceStream("알아들을 수 가 없습니다. 다시한번 말씀 해주세요.", output_file)

		MS.play_file(output_file)

if __name__ == '__main__':
	main()