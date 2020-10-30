#!/usr/bin/env python3
import threading
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO
# Setup board mode
GPIO.setmode(GPIO.BCM)
btn_increase=23
GPIO.setup(btn_increase, GPIO.IN, pull_up_down=GPIO.PUD_UP)
btn_value=0

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

print('Runtime	'+'Temp Reading	'+'temp	')
x=0
def btn_increase_pressed():
    if btn_value !=2:
        btn_value=btn_value+1
    else:
        btn_value=0
# Setup debouncing and callbacks
GPIO.add_event_detect(btn_increase, GPIO.RISING, callback = btn_increase_pressed , bouncetime=200)

def print_temp_thread():
    """
    This function prints the temperature to the screen every five seconds
    """
    global x
    if (btn_value==0):
        thread = threading.Timer(10.0, print_temp_thread)
        x = x + 10
    elif (btn_value==1):
        thread = threading.Timer(5.0, print_temp_thread)
        x=x+5
    else:
        thread = threading.Timer(1.0, print_temp_thread)
        x=x+1
    thread.daemon = True  # Daemon threads exit when the program does
    thread.start()
    
    Temp = ((chan.voltage - (0.5))/0.01)
    Temp = round(Temp, 2)
    print(x, 's	', chan.value, '		', Temp, 'C')
        
    

if __name__ == "__main__":
    print_temp_thread() # call it once to start the thread
    
    # Tell our program to run indefinitely
    while True:
        pass