import os, pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def readData(slot):				# slot is the time slot ;)
	try:
		dataFile = open([BASE_DIR+"/scoreboard/team_data1.dat", BASE_DIR+"/scoreboard/team_data2.dat",][slot-1], "rb")
		data = pickle.load(dataFile)
		dataFile.close()
		return data
	except:
		readData(slot)
	

def dumpData(slot,data):
	try:
		dataFile = open([BASE_DIR+"/scoreboard/team_data1.dat", BASE_DIR+"/scoreboard/team_data2.dat",][slot-1], "wb")
		pickle.dump(data, dataFile, protocol=2)
		dataFile.close()
	except:
		dumpData(slot,data)
