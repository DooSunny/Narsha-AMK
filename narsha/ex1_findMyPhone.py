#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Date:2019.04.01
Example 5: 휴대폰 호출 예제
"""
from __future__ import print_function

import ex2_getVoice2Text as gv2t
import ex1_kwstest as kws

import time

import requests

'''
본 예제는 1번, 2번, 4번, 6번 예제에 
사용자 인증 정보가 기재되어야 정상 동작합니다.
(CLIENT_ID, CLIENT_KEY, CLIENT_SECRET)
'''

key = 'maker.ifttt.com 에서 키를 발급받은 후 붙혀넣기';

def main():
	#Example7 KWS+STT

	KWSID = ['기가지니', '지니야', '친구야', '자기야']
	while 1:
		recog = kws.test(KWSID[0])
		if recog == 200:
			print('KWS Dectected ...\n Start STT...')
			text = gv2t.getVoice2Text()
			print('Recognized Text: '+ text)
			time.sleep(0.5)
			if text == '휴대폰 찾아줘':
				find_my_phone()
		else:
			print('KWS Not Dectected ...')

def find_my_phone():
    requests.get("https://maker.ifttt.com/trigger/noti/with/key/" + key)

if __name__ == '__main__':
    main()
