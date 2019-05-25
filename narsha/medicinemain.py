import medicine as med
import call_stt
import threading
import re
def main():
	t1 = threading.Thread(target = calling)
	output_file = "testtts.wav"
	i=0
	while True :
		bf = 1
		lc = 1
		dn = 1
		now=datetime.datetime.now()
		if (med.breakfirst == now.hour):
			if (medbreakfirstminute == now.minute):
				if (bf == 1):
					med.movemotor()
					call_stt.getText2VoiceStream("아침약 먹을 시간입니다.", output_file)
		elif (med.launch == now.hour):
			if (medbreakfirstminute == now.minute):
				if (lc == 1):
					med.movemotor()
					call_stt.getText2VoiceStream("점심약 먹을 시간입니다.", output_file)
		elif (med.dinner == now.hour):
			if (meddinnerminute == now.minute):
				if (dn == 1):
					med.movemotor()
					call_stt.getText2VoiceStream("저녁약 먹을 시간입니다.", output_file)
					if (med.movement):
def calling():
	while True :
		text=call_stt.Call()
		if (아침 in text):
			numbers = re.findall("\d+",text)
			print(numbers)
			if((오후 in text) or (numbers[0] > 12)):
				med.setbreakfirst(med.medicine,numbers[0],1)
			else
				med.setbreakfirst(med.medicine,numbers[0],0)
			if(분 in text):
				med.setbreakfirstminute(med.medicine,numbers[1])
		if(점심 in text):
			numbers = re.findall("\d+",text)
			print(numbers)
			if((오후 in text) or (numbers[0] > 12)):
				med.setlaunch(med.medicine,numbers[0],1)
			else
				med.setlaunch(med.medicine,numbers[0],0)
			if(분 in text):
				med.setlaunchminute(med.medicine,numbers[1])
		if (저녁 in text):
			numbers = re.findall("\d+",text)
			print(numbers)
			if((오후 in text) or (numbers[0] > 12)):
				med.setdinner(med.medicine,numbers[0],1)
			else
				med.setdinner(med.medicine,numbers[0],0)
			if(분 in text):
				med.setdinnerminute(med.medicine,numbers[1])
		else:
			call_stt.getText2VoiceStream("알아들을 수 가 없습니다. 다시한번 말씀 해주세요.", output_file)

		MS.play_file(output_file)



if __name__ == '__main__':
	main()
