import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
ser.flushInput()
print ser.readline()
