from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
   issue = models.TextField()
   created_by = models.ForeignKey(User, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now = True)
   associated_project  = models.ForeignKey('Project', on_delete=models.CASCADE)
   status = models.BooleanField()


class Project(models.Model):
   name = models.CharField(max_length = 50)
   description = models.TextField()
   devs = models.ManyToManyField(User)
   image = models.ImageField(upload_to='images')


class ResolvedTicket(models.Model):
   issue = models.ForeignKey(Ticket, on_delete=models.CASCADE)
   solution = models.TextField()
   solved_by = models.ForeignKey(User, on_delete=models.CASCADE)
   sloved_at = models.DateTimeField(auto_now = True)


class Log(models.Model):
   issue = models.ForeignKey('Ticket', on_delete=models.CASCADE)
   solution = models.ForeignKey('ResolvedTicket', on_delete=models.CASCADE)


   



