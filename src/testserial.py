import serial
import shared
ser = shared.init()
while 1:
	print shared.read(ser)
