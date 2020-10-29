#!/usr/bin/env python3
import threading
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

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

def print_temp_thread():
    """
    This function prints the temperature to the screen every five seconds
    """
    thread = threading.Timer(5.0, print_temp_thread)
    thread.daemon = True  # Daemon threads exit when the program does
    thread.start()
    global x
    Temp = ((chan.voltage - (0.5))/0.01)
    print(x, 's	', chan.value, '		', Temp, 'C')
    x = x + 10

if __name__ == "__main__":
    print_temp_thread() # call it once to start the thread
    
    # Tell our program to run indefinitely
    while True:
        pass