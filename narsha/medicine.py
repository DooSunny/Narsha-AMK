import RPi.GPIO as GPIO
import time

class medicine:

	breakfirst = 8
	movement = 0
	launch = 12
	dinner = 6
	barkfirstminute = 0
	launchminute = 0
	dinnerminute = 0
	GPIO.setmode(GPIO.BOARD)
	
	control_pins = [7,11,13,15]
	for pin in control_pins:
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin,0)
	halfstep_seq = [
		[1,0,0,0],
		[1,1,0,0],
		[0,1,0,0],
		[0,1,1,0],
		[0,0,1,0],
		[0,0,1,1],
		[0,0,0,1],
		[1,0,0,1]
	]
	def setbreakfirst(self,time,morning):
		if morning==1:
			self.breakfirst = time
		elif morning==0:
			self.breakfirst = time+12
	def setlaunch(self,time,morning):
		if morning==1:
			self.launch = time
		elif morning==0:
			self.launch = time+12
	def setdinner(self,time,morning):
		if morning==1:
			self.dinner = time
		elif morning==0:
			self.dinner = time+12
	def setbreakfirstminute(self,time):
		self.breakfirstminute = time
	def setlaunchminute(self,time):
		self.launchminute = time
	def setdinnerminute(self,time):
		self.dinnerminute = time
	def movemotor(self):
		for cnt in range(500):
			for pin in range(4):
				GPIO.output(self.control_pins[pin], self.halfstep_seq[self.movement%8][pin])
			time.sleep(1)
			self.movement+=1

