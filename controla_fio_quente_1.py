
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

input_pin = 4
output_pin = 26


GPIO.setup(input_pin,GPIO.IN, GPIO.PUD_UP)
GPIO.setup(output_pin,GPIO.OUT)
GPIO.setwarnings(False)

# apenas para trasnformar em milisegundos
mili = 0.001 

# delay é o intervalo de tempo de envio da tesão de 5V para o optoaclopador 
global delay
delay = 0.9
delay = delay*mili


def pulse(intervalo):
    GPIO.output(output_pin,GPIO.HIGH)
    time.sleep(intervalo)
    GPIO.output(output_pin,GPIO.LOW)
    print(intervalo,"este é odelay")

    

global cont
cont = 0

def onRising(nonsense):
    global cont
    global delay
    pulse(delay)
    cont = cont+1
    print(cont)
    
    
t_end = time.time()+10
#while time.time() < t_end:
GPIO.add_event_detect(input_pin, GPIO.RISING, callback=onRising)

 
 
time.sleep(10)
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
