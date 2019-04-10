#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example 1: GiGA Genie Keyword Spotting"""

from __future__ import print_function

import grpc
import gigagenieRPC_pb2
import gigagenieRPC_pb2_grpc
import MicrophoneStream as MS
import user_auth as UA
import os
import audioop
from ctypes import *
import RPi.GPIO as GPIO
import ktkws # KWS
import MicrophoneStream as MS
import datetime

KWSID = ['기가지니', '지니야', '친구야', '자기야']
RATE = 16000
CHUNK = 512

HOST = 'gate.gigagenie.ai'
PORT = 4080
RATE = 16000
CHUNK = 512

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(31, GPIO.OUT)
btn_status = False

def callback(channel):  
	print("falling edge detected from pin {}".format(channel))
	global btn_status
	btn_status = True
	print(btn_status)

GPIO.add_event_detect(29, GPIO.FALLING, callback=callback, bouncetime=10)

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
def py_error_handler(filename, line, function, err, fmt):
  dummy_var = 0
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
asound = cdll.LoadLibrary('libasound.so')
asound.snd_lib_error_set_handler(c_error_handler)

def detect():
	with MS.MicrophoneStream(RATE, CHUNK) as stream:
		audio_generator = stream.generator()

		for content in audio_generator:

			rc = ktkws.detect(content)
			rms = audioop.rms(content,2)
			#print('audio rms = %d' % (rms))

			if (rc == 1):
				MS.play_file("../data/sample_sound.wav")
				return 200

def test(key_word = '기가지니'):
	rc = ktkws.init("../data/kwsmodel.pack")
	print ('init rc = %d' % (rc))
	rc = ktkws.start()
	print ('start rc = %d' % (rc))
	print ('\n호출어를 불러보세요~\n')
	ktkws.set_keyword(KWSID.index(key_word))
	rc = detect()
	print ('detect rc = %d' % (rc))
	print ('\n\n호출어가 정상적으로 인식되었습니다.\n\n')
	ktkws.stop()
	return rc

def generate_request():
    with MS.MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
    
        for content in audio_generator:
            message = gigagenieRPC_pb2.reqVoice()
            message.audioContent = content
            yield message
            
            rms = audioop.rms(content,2)
            #print_rms(rms)

def getVoice2Text():	
    print ("\n\n음성인식을 시작합니다.\n\n종료하시려면 Ctrl+\ 키를 누루세요.\n\n\n")
    channel = grpc.secure_channel('{}:{}'.format(HOST, PORT), UA.getCredentials())
    stub = gigagenieRPC_pb2_grpc.GigagenieStub(channel)
    request = generate_request()
    resultText = ''
    for response in stub.getVoice2Text(request):
        if response.resultCd == 200: # partial
            print('resultCd=%d | recognizedText= %s' 
                  % (response.resultCd, response.recognizedText))
            resultText = response.recognizedText
        elif response.resultCd == 201: # final
            print('resultCd=%d | recognizedText= %s' 
                  % (response.resultCd, response.recognizedText))
            resultText = response.recognizedText
            break
        else:
            print('resultCd=%d | recognizedText= %s' 
                  % (response.resultCd, response.recognizedText))
            break

    # print ("\n\n인식결과: %s \n\n\n" % (resultText))
    return resultText

def getText2VoiceStream(inText,inFileName):

	channel = grpc.secure_channel('{}:{}'.format(HOST, PORT), UA.getCredentials())
	stub = gigagenieRPC_pb2_grpc.GigagenieStub(channel)

	message = gigagenieRPC_pb2.reqText()
	message.lang=0
	message.mode=0
	message.text=inText
	writeFile=open(inFileName,'wb')
	for response in stub.getText2VoiceStream(message):
		if response.HasField("resOptions"):
			print ("\n\nResVoiceResult: %d" %(response.resOptions.resultCd))
		if response.HasField("audioContent"):
			print ("Audio Stream\n\n")
			writeFile.write(response.audioContent)
	writeFile.close()
	return response.resOptions.resultCd

#==========================================================================================================
# what time is it?
def Clock_hour(): # 시간 [시]
	time=["한","두","세","네","다섯","여섯","일곱","여덟","아홉","열","열한","열두"] # 만약 안해줄시 시간을 물을때 "한시"가 아니라 "일시"라고 대답한다
	now=datetime.datetime.now()
	return time[(now.hour -1)%12]

def Clock_minute(): # 시간 [분]
	now=datetime.datetime.now()
	return now.minute

#===========================================================================================================
def main():
	output_file = "testtts.wav"
	text=""
	while True :
		test_return = test()

		if(int(test_return) == 200):
			text = getVoice2Text()
			text=text.replace(" ","")
			print("text : %s"%text)

		text = text.encode("utf-8")
		# print("type : %s" %type(text))

		if("안녕" in text):
			getText2VoiceStream("안녕하세요. 반갑습니다.", output_file)
		else if("이름" in text):
			getText2VoiceStream("제 이름은 기가지니입니다.", output_file)

		else if(("몇시" in text) or ("시간" in txt) ):
			hour=Clock_hour()
			minute=Clock_minute()
			getText2VoiceStream("지금은 "+hour+"시, "+str(minute)+"분 입니다.", output_file)

		else:
			getText2VoiceStream("알아들을 수 가 없습니다. 다시한번 말씀 해주세요.", output_file)

		MS.play_file(output_file)
		text=""

if __name__ == '__main__':
	main()