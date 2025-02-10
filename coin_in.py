import RPi.GPIO as GPIO
import time
from signal import pause

# ธนบัตร
#สาย สีน้ำเงิน Sensor PWM = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
counter = 0
time_start = time.time()
time_end = time.time()
status_gpi = 0
MONEY = 0

def sensor_callback(channel):
    global counter,MONEY
    checkGPOI = GPIO.input(channel)
    if checkGPOI == 0 :
       counter = counter + 1
       MONEY = MONEY + 1
       print('IN',MONEY)

GPIO.add_event_detect(12,GPIO.BOTH,callback=sensor_callback)
print("Start")
pause()
