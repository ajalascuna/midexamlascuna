from django.db import models

# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

    def __str__(self):
        return '{}'.format(str(self.name))

class Candidate(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    #position = models.TextField(default=None,blank=True,null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name = 'candidates', blank=True, null=True)
    birthdate = models.DateField('birthdate')
    platform = models.TextField(max_length=100)

    def __str__(self):
        return 'Firstname: {}'.format(str(self.firstname))

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name = 'votes')
    vote_datetime = models.DateTimeField('vote_datetime')
