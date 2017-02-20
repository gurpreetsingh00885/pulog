from django.http import HttpResponse
from django.shortcuts import render
from .utils import dumpData, readData
from django.views import View

class index(View):
	def get(self,request, teams = None, *args, **kwargs):
		possible =["ab,ac,ad,ae,af,bc,bd,be,bf,cd,ce,cf,de,df,ef".split(',') + list(map(lambda x:x[::-1], "ab,ac,ad,ae,af,bc,bd,be,bf,cd,ce,cf,de,df,ef".split(','))),
		"gh,gi,gj,gk,gl,hi,hj,hk,hl,ij,ik,il,jk,jl,kl".split(',') + list(map(lambda x:x[::-1], "gh,gi,gj,gk,gl,hi,hj,hk,hl,ij,ik,il,jk,jl,kl".split(','))),]
		if teams not in possible[0]+possible[1]:
			return HttpResponse("Invalid Team match!")
		save=open("abc.txt", 'w')
		save.write(teams)
		save.close()
		slot = 1 if teams in possible[0] else 2
		data = readData(slot)
		context = {
			'team_1' : data[teams[0]][0]+" (#%s)" %(teams[0]),
			'team_2' : data[teams[1]][0]+" (#%s)" %(teams[1]),
			'team_1_wins' : data[teams[0]][1],
			'team_2_wins' : data[teams[1]][1],
			'team_1_losses' : data[teams[0]][2],
			'team_2_losses' : data[teams[1]][2],
		}
		return render(request , "score/score_admin.html", context)

	def post(self, request, *args, **kwargs):
		possible =["ab,ac,ad,ae,af,bc,bd,be,bf,cd,ce,cf,de,df,ef".split(',') + list(map(lambda x:x[::-1], "ab,ac,ad,ae,af,bc,bd,be,bf,cd,ce,cf,de,df,ef".split(','))),
		"gh,gi,gj,gk,gl,hi,hj,hk,hl,ij,ik,il,jk,jl,kl".split(',') + list(map(lambda x:x[::-1], "gh,gi,gj,gk,gl,hi,hj,hk,hl,ij,ik,il,jk,jl,kl".split(','))),]
		save=open("abc.txt", 'r')
		teams = save.readline()
		save.close()
		slot = 1 if teams in possible[0] else 2
		data = readData(slot)
		if('add_team_1' in request.POST):
			data[teams[0]][1]+=1
			dumpData(slot, data)
		if('sub_team_1' in request.POST):
			data[teams[0]][1]-=1
			dumpData(slot, data)
		if('add_team_2' in request.POST):
			data[teams[1]][1]+=1
			dumpData(slot, data)
		if('sub_team_2' in request.POST):
			data[teams[1]][1]-=1
			dumpData(slot, data)

		if('add_team_1_loss' in request.POST):
			data[teams[0]][2]+=1
			dumpData(slot, data)
		if('sub_team_1_loss' in request.POST):
			data[teams[0]][2]-=1
			dumpData(slot, data)
		if('add_team_2_loss' in request.POST):
			data[teams[1]][2]+=1
			dumpData(slot, data)
		if('sub_team_2_loss' in request.POST):
			data[teams[1]][2]-=1
			dumpData(slot, data)


		data = readData(slot)
		context = {
			'team_1' : data[teams[0]][0]+" (#%s)" %(teams[0]),
			'team_2' : data[teams[1]][0]+" (#%s)" %(teams[1]),
			'team_1_wins' : data[teams[0]][1],
			'team_2_wins' : data[teams[1]][1],
			'team_1_losses' : data[teams[0]][2],
			'team_2_losses' : data[teams[1]][2],
		}
		return render(request , "score/score_admin.html", context)