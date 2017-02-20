from django.http import HttpResponse
from .utils import dumpData, readData
def index(request, teams = None):
	possible =["ab,ac,ad,ae,af,bc,bd,be,bf,cd,ce,cf,de,df,ef".split(',') + list(map(lambda x:x[::-1], "ab,ac,ad,ae,af,bc,bd,be,bf,cd,ce,cf,de,df,ef".split(','))),]
	print(possible[0])
	if teams not in possible[0]:
		return HttpResponse("Invalid Team match!")
	slot = 1 if teams in possible[0] else 2
	data = readData(slot)
	return HttpResponse("%s Wins: %d<br/>%s Wins: %d" %(data[teams[0]][0], data[teams[0]][1], data[teams[1]][0], data[teams[1]][1]))