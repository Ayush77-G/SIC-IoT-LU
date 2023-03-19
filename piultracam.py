import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from time import sleep

TRIG_PIN = 11
ECHO_PIN = 12
GPIO.setmode(GPIO.BCM)
cam=PiCamera()
while True:
    print("Checking the distance")
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    GPIO.output(TRIG_PIN, False)
    print("Calming Down")
    time.sleep(0.2)
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print("distance:", distance, "cm")
    time.sleep(2)

    if 0 < distance < 400:
        cam.start_preview()
        sleep(2)
        cam.capture('/home/pi/Desktop/image.jpg')
        cam.stop_preview()
    time.sleep(2)

