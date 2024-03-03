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
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now = True)
    file = models.FileField()
    status = models.CharField(max_length = 50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class ProjectDevs(models.Model):
    dev = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ManyToManyField(User, related_name='dev_project')


class Log(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    resolved_by = models.ForeignKey(User, on_delete=models.CASCADE)
    resolved_at = models.DateTimeField(auto_now = True)
