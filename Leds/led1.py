"""
Purpose: blink a led ten times in Raspberry PI3 connecting anode on GPIO 17 (using a resistor) and catode connected to
         Ground.
Programed: Roger Manich
Date: 2018-01-29

Remarks: On non Raspberry PI you should receive an exception
"""
from gpiozero import LED
from time import sleep


try:
    #Configure GPIO 17 to operate with LED
    led = LED(17)
    #blink 10 times
    for x in range(1,10):
        print("Led is on. Round {1}".format(x))
        led.on()
        sleep(1)
        led.off()
        print("Led is off, Round {1}".format(x))
        sleep(1)
except:
    print("Unexpected Error or you are not running it on Raspberry Pi 3")



