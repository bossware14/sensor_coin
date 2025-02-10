import RPi.GPIO as GPIO
import time
from signal import pause

# ธนบัตร
#สาย สีน้ำเงิน Sensor PWM = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

time_start = time.time()
time_end = time.time()
counter = 0
status_gpi = 0
MONEY = 0

def sensor_callback(channel):
    global counter,MONEY,status_gpi,time_start,time_end
    checkGPOI = GPIO.input(channel)
    time_start = round(time.time(),1)
    if checkGPOI == 1 :
       time_start = round(time.time(),1)
       status_gpi = checkGPOI
       MONEY =0
       counter =0
    if checkGPOI == 0 :
       time_end = round(time.time(),1)
       status_gpi = checkGPOI
       checktime = round(time_end-time_start,1)

    if checkGPOI == 0 and status_gpi == 0 and checktime == 0:
       MONEY = MONEY +10
       counter = counter +1
       status_gpi = 1
    if MONEY >= 20 :
       print(MONEY)

#GPIO.add_event_detect(12,GPIO.BOTH,callback=sensor_callback)
GPIO.add_event_detect(12,GPIO.FALLING,callback=sensor_callback)
print("Start")
pause()
