#Connect Ground and Pin 7

#import the GPIO and time package
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT) #GPIO4 on PIN7
# loop through 10 times, on/off for 1 second
for i in range(10):
    GPIO.output(7,True)
    time.sleep(1)
    GPIO.output(7,False)
    time.sleep(1)
GPIO.cleanup()
