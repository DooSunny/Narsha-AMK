from medicine import medicine
import call_stt
import threading
import re
import datetime

def main(med):
	t1 = threading.Thread(target = calling(med))
	t1.daemon=True
	t1.start()
	output_file = "testtts.wav"
	i=0
	while True :
		bf = 1
		lc = 1
		dn = 1
		now=datetime.datetime.now()
		if (med.breakfirst == now.hour):
			if (med.breakfirstminute == now.minute):
				if (bf == 1):
					med.movemotor()
					call_stt.getText2VoiceStream("아침약 먹을 시간입니다.", output_file)
		elif (med.launch == now.hour):
			if (med.launchminute == now.minute):
				if (lc == 1):
					med.movemotor()
					call_stt.getText2VoiceStream("점심약 먹을 시간입니다.", output_file)
		elif (med.dinner == now.hour):
			if (med.dinnerminute == now.minute):
				if (dn == 1):
					med.movemotor()
					call_stt.getText2VoiceStream("저녁약 먹을 시간입니다.", output_file)
def calling(med):
	while True :
		text=call_stt.Call()
		if ("아침" in text):
			numbers = re.findall("\d+",text)
			print(type(numbers))
			print(type(text))
			print(type("오후"in text))
			if(("오후" in text) or (int(numbers[0])> 12)):
				med.setbreakfirst(med,numbers[0],1)
			else:
				med.setbreakfirst(med,numbers[0],0)
			if("분" in text):
				med.setbreakfirstminute(med,numbers[1])
		if("점심" in text):
			numbers = re.findall("\d+",text)
			print(numbers)
			if(("오후" in text) or (numbers[0] > 12)):
				med.setlaunch(med,numbers[0],1)
			else:
				med.setlaunch(med,numbers[0],0)
			if("분" in text):
				med.setlaunchminute(med,numbers[1])
		if ("저녁" in text):
			numbers = re.findall("\d+",text)
			print(numbers)
			if(("오후" in text) or (numbers[0] > 12)):
				med.setdinner(med,numbers[0],1)
			else:
				med.setdinner(med,numbers[0],0)
			if("분" in text):
				med.setdinnerminute(med,numbers[1])
		else:
			call_stt.getText2VoiceStream("알아들을 수 가 없습니다. 다시한번 말씀 해주세요.", output_file)

		MS.play_file(output_file)



if __name__ == '__main__':
	med = medicine()
	main(med)
