#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example 1: GiGA Genie Keyword Spotting"""
import MicrophoneStream as MS
import ex1_Clock
import call_stt
import newspaperdaum as news
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
		else:
			call_stt.getText2VoiceStream("알아들을 수 가 없습니다. 다시한번 말씀 해주세요.", output_file)

		MS.play_file(output_file)

if __name__ == '__main__':
	main()