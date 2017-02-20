import os, pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def readData(slot):				# slot is the time slot ;)
	dataFile = open([BASE_DIR+"/scoreboard/team_data1.dat", BASE_DIR+"/scoreboard/team_data2.dat",][slot-1], "rb")
	print([os.path.join(BASE_DIR, "scoreboard/team_data1.dat"), os.path.join(BASE_DIR, "scoreboard/team_data1.dat"),][slot-1])
	data = pickle.load(dataFile)
	dataFile.close()
	return data

def dumpData(slot,data):
	dataFile = open([BASE_DIR+"team_data1.dat", BASE_DIR+"team_data2.dat",][slot-1], "wb")
	pickle.dump(data, dataFile)
	dataFile.close()
