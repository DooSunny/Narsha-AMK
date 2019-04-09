import ex1_call_stt_tts as cts

def main():
	output_file = "testtts.wav"
	
	test_return=cts.test()
	
	if(int(test_return)==200):
		text = cts.getVoice2Text()
		print("text : %s"%text)

	if(text):
		cts.getText2VoiceStream("안녕하세요. 반갑습니다.",output_file)
		cts.play_file(output_file)

	text=False

if __name__ == '__main__':
	main()