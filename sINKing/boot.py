try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

from inkplate6_PLUS import Inkplate
from image import *
import time

display = Inkplate(Inkplate.INKPLATE_1BIT)

def updatePaper(ssid, password, station):
    display.clearDisplay();    #Clear everything from epaper frame buffer
    display.printText(10, 10, "Server is up and running!")
    display.fillRect(10, 240, 780, 4, 0)
    display.printText(10, 300, "User said:") #Print out what user typed in web page
    #display.print(txt)
    display.display(); #Send everything to screen (refresh the screen)

if __name__ == "__main__":
    # Must be called before using, line in Arduino
    display.begin()
    display.clearDisplay()
    display.display()
    display.setTextSize(10)
    display.printText(100, 100, "Say something!")
    display.setTextSize(3)
    display.printText(100, 300, "Ernie's Inkplate server test")
    display.display()

    ssid = 'TP-Link_3CA4'
    password = '10906279'

    station = network.WLAN(network.STA_IF)

    station.active(True)
    station.connect(ssid, password)

    while station.isconnected() == False:
      pass

    print('Connection successful')
    print(station.ifconfig())

    led = Pin(2, Pin.OUT)

    updatePaper(ssid, password, station)

