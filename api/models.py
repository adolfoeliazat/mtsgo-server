from django.db import models
from django.core.validators import validate_comma_separated_integer_list, MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.conf import settings
from mtsgo.helpers import handle_exception
import time


class Player(models.Model):
    account = models.ForeignKey(User)
    nickname = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20, default='')
    name = models.CharField(max_length=20, default='')
    positionx = models.FloatField(default=0.0, validators = [MinValueValidator(-90.0), MaxValueValidator(90.0)])
    positiony = models.FloatField(default=0.0, validators = [MinValueValidator(-180.0), MaxValueValidator(180.0)])
    positionz = models.FloatField(default=0.0)
    score = models.IntegerField(default=0)
    questionHistory = models.CharField(max_length=255, validators=[validate_comma_separated_integer_list])

    def getPosition(self):
        return (self.positionx, self.positiony, self.positionz)

    def addQuestionToHistory(self, qid):
        qids = []
        if len(self.questionHistory) > 0:
            try:
                qids = self.questionHistory.split(',')
            except ValueError as e:
                # This should not happen as entries are validated before insertion by Django.
                pass
        if len(qids) >= getattr(settings, 'MTSGO_PLAYER_HISTORY_LIMIT', 10):
            qids.pop(0)
        qids.append(str(qid))
        self.questionHistory = ','.join(qids)


    def __str__(self):
        return self.nickname


class Question(models.Model):
    # Il faut garder à l'esprit que ça pourrait contenir du Latex.
    questionText = models.CharField(max_length=255)
    answer1 = models.CharField(max_length=100)
    answer2 = models.CharField(max_length=100)
    answer3 = models.CharField(max_length=100)
    answer4 = models.CharField(max_length=100)
    CHOICES = (
        (1, answer1),
        (2, answer2),
        (3, answer3),
        (4, answer4),
    )
    rightAnswer = models.IntegerField(choices=CHOICES)
    difficulty = models.IntegerField()
    topic = models.CharField(max_length=20)  # theme de la question
    score = models.IntegerField()  # points rapportes

    def __str__(self):
        return self.questionText


class Spot(models.Model):
    centrex = models.FloatField(validators = [MinValueValidator(-90.0), MaxValueValidator(90.0)])
    centrey = models.FloatField(validators = [MinValueValidator(-180.0), MaxValueValidator(180.0)])
    centrez = models.FloatField(default=0)
    rayon = models.IntegerField(validators=[MinValueValidator(0)])
    currentQuestion = models.ForeignKey('Question')
    questionList = models.CharField(max_length=100, validators=[validate_comma_separated_integer_list])
    startTime = models.IntegerField(default=time.time)
    delay = models.IntegerField()

    def getPosition(self):
        return (self.centrex, self.centrey, self.centrez)

    def __str__(self):
        return 'x=' + str(self.centrex) + ' y=' + str(self.centrey) + ' z=' + str(self.centrez)


class ExclusionZone(models.Model):
    name = models.CharField(max_length=20)
    points = models.TextField()

    def __str__(self):
        return self.name
