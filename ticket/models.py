from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images', default='')
    

class Ticket(models.Model):
    CHOICE_ONE = 'In Progress'
    CHOICE_TWO = 'Completed'
    CHOICE_THREE = 'Failed'
    YOUR_CHOICES = [
        (CHOICE_ONE, 'Work In Progress'),
        (CHOICE_TWO, 'Ticket Solved Successfully'),
        (CHOICE_THREE, 'Failed to solve'),
    ]
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    file = models.FileField(upload_to='uploads/')
    status = models.CharField(max_length=100, choices=YOUR_CHOICES, default=CHOICE_ONE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class ProjectDevs(models.Model):
    dev = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ManyToManyField(Project, related_name='dev_project')

    project = models.ForeignKey()

class Log(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    resolved_by = models.ForeignKey(User, on_delete=models.CASCADE)
    resolved_at = models.DateTimeField(auto_now = True)