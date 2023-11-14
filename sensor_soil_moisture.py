import RPi.GPIO as GPIO
import time
pin = 12 #GPIO18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN)         #Read output from soil moisture sensor
def callback(pin):
	i=GPIO.input(pin)
	print("sensor output", i)
	if i==1:
		print("Watering is not needed for now!")
	else:
		print("Watering is needed!")
GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(pin, callback)

while True:
	'''
	i=GPIO.input(pin)
	print("sensor message:", i)
	if(GPIO.event_detected(pin)):
		print("Something happened")
	'''
	time.sleep(0)
