#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO_RPi
# GPIO pin assign
SW_ENCA= 22
SW_ENCB= 23

def callback(callback):
    re = (GPIO_RPi.input(SW_ENCA) &1)
    re += (GPIO_RPi.input(SW_ENCB) &1)<<1
    print(re)

def main():
    GPIO_RPi.setwarnings(False)
    GPIO_RPi.setmode(GPIO_RPi.BCM)
    # GPIO initialize
    GPIO_RPi.setup(SW_ENCA, GPIO_RPi.IN)
    GPIO_RPi.setup(SW_ENCB, GPIO_RPi.IN)
    GPIO_RPi.add_event_detect(SW_ENCA, GPIO_RPi.BOTH, callback=callback, bouncetime=5)
    GPIO_RPi.add_event_detect(SW_ENCB, GPIO_RPi.BOTH, callback=callback, bouncetime=5)
    try:
        while(True):
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("break")
        GPIO_RPi.cleanup()

if __name__ == "__main__":
    main()