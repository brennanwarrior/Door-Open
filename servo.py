import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
pwm=GPIO.PWM(12,50)
pwm.start(0)
def SetAngle(angle):
    duty=angle/18+2
    GPIO.output(12,True)
    pwm.ChangeDutyCycle(duty)
    sleep(2)
    GPIO.output(12,False)
    pwm.ChangeDutyCycle(0)
def open_door():
    SetAngle(180)
    SetAngle(0)
    SetAngle(180)
    SetAngle(0)
