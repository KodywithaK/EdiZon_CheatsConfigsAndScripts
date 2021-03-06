## bin ##

import edizon

saveFileBuffer = edizon.getSaveFileBuffer()

def getValueFromSaveFile():
	strArgs = edizon.getStrArgs()
	intArgs = edizon.getIntArgs()
	indirectAddress = int(strArgs[0], 16)
	address = int(strArgs[1], 16)
	addressSize = intArgs[0]
	valueSize = intArgs[1]
	
	offset = 0
	value = 0
		
	if indirectAddress != 0:
		for i in range(0, addressSize):
			offset = offset | (saveFileBuffer[indirectAddress + i] << i * 8)
		
	for i in range(0, valueSize):
		value = value | (saveFileBuffer[offset + address + i] << i * 8)
		
	return value

def setValueInSaveFile(value):
	strArgs = edizon.getStrArgs()
	intArgs = edizon.getIntArgs()
	indirectAddress = int(strArgs[0], 16)
	address = int(strArgs[1], 16)
	addressSize = intArgs[0]
	valueSize = intArgs[1]
	
	offset = 0
	
	if indirectAddress != 0:
		for i in range(0, addressSize):
			offset = offset | (saveFileBuffer[indirectAddress + i] << (i * 8))
		
	for i in range(0, valueSize):
		saveFileBuffer[offset + address + i] = (value & (0xFF << i * 8)) >> (i * 8)

def getModifiedSaveFile():
	return saveFileBuffer

