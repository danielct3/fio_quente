
import RPi.GPIO as GPIO

import time


GPIO.setmode(GPIO.BCM)

input_pin = 4

GPIO.setup(input_pin,GPIO.IN, GPIO.PUD_UP)

global cont
cont = 0

def onRising(ishi):
    global cont
    cont = cont+1
t_end = time.time()+10
#while time.time() < t_end:
GPIO.add_event_detect(input_pin, GPIO.RISING, callback=onRising)

 
 
time.sleep(100
)
GPIO.cleanup()
print(cont)


'''
a = range(1000)
for i in a:
    state = GPIO.input(input_pin)
    if state == GPIO.HIGH:
        print("high")
    else:
        print("low")
        
        

time.sleep(1)

'''
