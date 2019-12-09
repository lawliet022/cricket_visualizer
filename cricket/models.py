from django.db import models

class Match(models.Model):
    TWENTY = 'T20'
    ODI = 'ODI'
    MATCH_TYPE_CHOICES = [
        (TWENTY,'Twenty Twenty'),
        (ODI, 'One Day Internation'),
    ]
    mId =  models.IntegerField(primary_key=True)
    matchDate = models.DateField()
    venue = models.CharField(max_length=1000, blank=True)
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    won = models.CharField(max_length=50)
    tossDecision = models.CharField(max_length=50)
    tossWon = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    matchType = models.CharField(
        max_length=3,
        choices=MATCH_TYPE_CHOICES,
        default=ODI,
    )

class MatchData(models.Model):
    mId = models.ForeignKey(Match,on_delete=models.CASCADE)
    teamBatting = models.CharField(max_length=50)
    over = models.IntegerField(default=0)
    ballNo = models.IntegerField(default=0)
    batsman = models.CharField(max_length=500)
    bowler = models.CharField(max_length=500)
    runTaken = models.IntegerField(default=0)
    extras = models.IntegerField(default=0)
    totalRuns = models.IntegerField(default=0)
    nonStriker = models.CharField(max_length=500)
    outcome = models.CharField(max_length=500,blank = True)

