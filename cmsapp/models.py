from django.db import models


class PageData(models.Model):
    title = models.CharField(max_length=25)
    message = models.TextField(max_length=500)
    lastupdate = models.DateTimeField(auto_now_add=True)

class UserData(models.Model):
    timecreated = models.DateTimeField(auto_now_add=True)
    record = models.CharField(max_length=100) 

