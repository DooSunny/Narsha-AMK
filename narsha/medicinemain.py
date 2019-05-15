import medicine as med
def main():
	output_file = "testtts.wav"
	i=0
	while True :
        bf = 1
        lc = 1
        dn = 1
	    now=datetime.datetime.now()
	    if med.breakfirst == now.hour:
            if medbreakfirstminute == now.minute:
                if bf == 1:
                    med.movemotor()
                    #말하는 무언가
        elif med.launch == now.hour:
            if medbreakfirstminute == now.minute:
                if lc == 1:
                    med.movemotor()
                    #말하는 무언가
        elif med.dinner == now.hour:
            if meddinnerminute == now.minute:
                if dn == 1:
                    med.movemotor()
                    #말하는 무언가
        
if __name__ == '__main__':
	main()
