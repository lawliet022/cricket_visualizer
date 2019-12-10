from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json

from .models import Match, MatchData
# Create your views here.


def index(request):
    return render(request, "cricket/index.html")


def getTeam1(request):
    data = request.GET.copy()

    match_type = data.get('match_type', '')
    # print(match_type)
    team1 = Match.objects.filter(matchType=match_type)
    team_names = set()
    for team in team1:
        team_names.add(team.team1)
    return JsonResponse({"data": {'teams': list(team_names)}})

def getTeam2(request):
    data = request.GET.copy()

    match_type = data.get('match_type', '')
    team1 = data.get('team1', '')
    if match_type and team1:
        teams2 = Match.objects.filter(matchType=match_type, team1=team1)
        team_names = set()
        for team in teams2:
            team_names.add(team.team2)
    return JsonResponse({"data": {'teams': list(team_names)}})

def getMatchDate(request):
    data = request.GET.copy()

    match_type = data.get('match_type', '')
    team1 = data.get('team1', '')
    team2 = data.get('team2', '')

    if match_type and team1 and team2:
        dates = Match.objects.filter(matchType=match_type, team1=team1, team2=team2)
        print(dates)
        date_list = set()
        for date in dates:
            date_list.add(date.matchDate)
        
    return JsonResponse({"data": {'dates': list(date_list)}})


def getData(request):

    data = request.GET.copy()

    match_type = data.get('match_type', '')
    team1 = data.get('team1', '')
    team2 = data.get('team2', '')
    date = data.get('date', '')

    if match_type and team1 and team2 and date:
        data1 = MatchData.objects.filter(mId__matchType=match_type, mId__team1=team1, mId__team2=team2, mId__matchDate=date, teamBatting=team1).exclude(outcome=' ')
        data2 = MatchData.objects.filter(mId__matchType=match_type, mId__team1=team1, mId__team2=team2, mId__matchDate=date, teamBatting=team2).exclude(outcome=' ')
        data_list1 = []
        data_list2 = []
        i=1
        for _ in data1:
            data_list1.append([_.over, i])
            i+=1
        i=1
        for _ in data2:
            data_list2.append([_.over, i])
            i+=1
    return JsonResponse({"data": {"team1": data_list1, "team2": data_list2}})


def getData2(request):

    data = request.GET.copy()

    match_type = data.get('match_type', '')
    team1 = data.get('team1', '')
    team2 = data.get('team2', '')
    date = data.get('date', '')

    if match_type and team1 and team2 and date:
        data1 = MatchData.objects.filter(mId__matchType=match_type, mId__team1=team1, mId__team2=team2, mId__matchDate=date, teamBatting=team1)
        data2 = MatchData.objects.filter(mId__matchType=match_type, mId__team1=team1, mId__team2=team2, mId__matchDate=date, teamBatting=team2)
        data_list1 = []
        data_list2 = []
        i=1
        prev = -1
        cur = 0
        for _ in data1:
            if _.over != prev:
                data_list1.append([i, cur])
                i+=1
                prev = _.over
            cur += _.totalRuns
                
        i=1
        prev = -1
        cur = 0
        for _ in data2:
            if _.over != prev:
                data_list2.append([i, cur])
                i+=1
                prev = _.over
            cur += _.totalRuns
            
    return JsonResponse({"data": {"team1": data_list1, "team2": data_list2}})

def getData3(request):

    data = request.GET.copy()

    match_type = data.get('match_type', '')
    team1 = data.get('team1', '')
    team2 = data.get('team2', '')
    date = data.get('date', '')

    if match_type and team1 and team2 and date:
        data1 = MatchData.objects.filter(mId__matchType=match_type, mId__team1=team1, mId__team2=team2, mId__matchDate=date, teamBatting=team1)
        data2 = MatchData.objects.filter(mId__matchType=match_type, mId__team1=team1, mId__team2=team2, mId__matchDate=date, teamBatting=team2)
        data_list1 = [0]*6
        data_list2 = [0]*6
        
        for _ in data1:
            if _.runTaken == 1:
                data_list1[0] += 1
            elif _.runTaken == 2:
                data_list1[1] += 2
            elif _.runTaken == 3:
                data_list1[2] += 3
            elif _.runTaken == 4:
                data_list1[3] += 4
            elif _.runTaken == 6:
                data_list1[4] += 6
            data_list1[5] += _.extras
        
        for _ in data2:
            if _.runTaken == 1:
                data_list2[0] += 1
            elif _.runTaken == 2:
                data_list2[1] += 2
            elif _.runTaken == 3:
                data_list2[2] += 3
            elif _.runTaken == 4:
                data_list2[3] += 4
            elif _.runTaken == 6:
                data_list2[4] += 6
            data_list2[5] += _.extras
        
        data_1 = []
        data_1.append(['1s',data_list1[0]])
        data_1.append(['2s',data_list1[1]])
        data_1.append(['3s',data_list1[2]])
        data_1.append(['4s',data_list1[3]])
        data_1.append(['6s',data_list1[4]])
        data_1.append(['Extras',data_list1[5]])

        data_2 = []
        data_2.append(['1s',data_list2[0]])
        data_2.append(['2s',data_list2[1]])
        data_2.append(['3s',data_list2[2]])
        data_2.append(['4s',data_list2[3]])
        data_2.append(['6s',data_list2[4]])
        data_2.append(['Extras',data_list2[5]])
        
            
    return JsonResponse({"data": {"team1": data_1, "team2": data_2}})

