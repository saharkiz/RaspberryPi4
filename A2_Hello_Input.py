import RPi.GPIO as GPIO  
from time import sleep 
#GPIO.BCM: Uses GPIO numbers ex: GPIO16
#GPIO.BOARD: Use pin numbers ex: 36
GPIO.setmode(GPIO.BCM)
port = 16 #GPIO16 on PIN36
GPIO.setup(port, GPIO.IN)
try:  
    while True:            #until CTRL+C  
        if GPIO.input(port):
            print "Port is 1/HIGH/True - LED ON"  
        else:  
            print "Port is 0/LOW/False - LED OFF"  
        sleep(0.5) 
finally:
    GPIO.cleanup()
