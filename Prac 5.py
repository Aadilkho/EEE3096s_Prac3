#!/usr/bin/env python3
import threading
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO
# Setup board mode


# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)
print(' ')
print('Runtime  '+'Temp Reading '+'temp ')
x=-10
c=10
count=0
start=0
def btn_setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(23, GPIO.RISING, callback = btn_pressed , bouncetime=200)
	
# Setup debouncing and callbacks

def start_setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(24, GPIO.RISING, callback = start_end , bouncetime=200)

def start_end():
	print('pressed')

def btn_pressed(channel):
	global c
	global count
	
	count=count+1 # and change the sample rate
	if count==1:
		c = 10
		print('Sampling every 10s')
	if count == 2:
		c = 5
		print('Sampling every 5s')
	if count == 3:
		c = 1
		print('Sampling every 1s')
		count = 0

		
def print_temp_thread():
	"""
	This function prints the temperature to the screen every five seconds
	"""
	global x
	global c
	x = x + c

	thread = threading.Timer(c, print_temp_thread)
	thread.daemon = True  # Daemon threads exit when the program does
	thread.start() 
	
	Temp = ((chan.voltage - (0.5))/0.01) # Equation obtained from MCP9700 datasheet
	Temp = round(Temp, 2) # round off the display temperature

	print(x, 's ', chan.value, '        ', Temp, 'C')
		
	

if __name__ == "__main__":
	btn_setup() #call to check the button press
	start_end()
	print_temp_thread() # call it once to start the thread
	

	# Tell our program to run indefinitely
	while True:
		pass