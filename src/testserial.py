import serial
import shared
ser = shared.init()
while 1:
	list = shared.read(ser)
	print list[0], list[1]
