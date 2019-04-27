import datetime
import ex1_call_stt_tts
# what time is it?
def Clock_hour(): # 시간 [시]
	time=["한","두","세","네","다섯","여섯","일곱","여덟","아홉","열","열한","열두"] # 만약 안해줄시 시간을 물을때 "한시"가 아니라 "일시"라고 대답한다
	now=datetime.datetime.now()
	return time[(now.hour -1)%12]

def Clock_minute(): # 시간 [분]
	now=datetime.datetime.now()
	return now.minute