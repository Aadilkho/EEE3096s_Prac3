import busio
2 import digitalio
3 import board
4 import adafruit_mcp3xxx.mcp3008 as MCP
5 from adafruit_mcp3xxx.analog_in import AnalogIn
6
7 # create the spi bus
8 spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
9
10 # create the cs (chip select)
11 cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
14 mcp = MCP.MCP3008(spi, cs)
15
16 # create an analog input channel on pin 0
17 chan = AnalogIn(mcp, MCP.P0)
18
19 print(’Raw ADC Value: ’, chan.value)
20 print(’ADC Voltage: ’ + str(chan.voltage) + ’V’)
