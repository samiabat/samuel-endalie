from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
class Level(models.Model):
    lebel  = models.CharField(max_length=15)

    def __str__(self):
        return str(self.lebel)

class Freelancer(models.Model):
    first_name = models.CharField(max_length = 30 , blank=True)
    last_name = models.CharField(max_length = 30, blank=True)
    username = models.CharField(max_length = 30, blank=True)
    email = models.EmailField(blank=True)
    location =  CountryField(default="Ethiopia", blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    bio = models.TextField(max_length= 40, blank=True)
    talent = models.TextField(max_length= 50 ,blank=True)
    password = models.CharField(max_length = 30, blank=True)
    password_confirmation = models.CharField(max_length = 30, blank=True)

    def __str__(self):
        return str(self.username)
        

        
class Employer(models.Model):
    first_name = models.CharField(max_length = 30 , blank=True)
    last_name = models.CharField(max_length = 30, blank=True)
    username = models.CharField(max_length = 30, blank=True)
    email = models.EmailField(blank=True)
    location =  CountryField(blank=True)
    talent = models.TextField(max_length= 50 ,blank=True)
    password = models.CharField(max_length = 30, blank=True)
    password_confirmation = models.CharField(max_length = 30, blank=True)

    def __str__(self):
        return str(self.username)

class Job(models.Model):
    job_title = models.CharField(max_length = 30, blank=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    salary = models.CharField(blank=True, max_length = 30)
    deadline = models.DateTimeField()
    job_description = models.TextField(max_length =500, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    restrictions = models.CharField(max_length = 20, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    class  Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.job_title)
class Message(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    message = models.TextField(max_length = 500, blank=True)

    def __str__(self):
        return str(message)


class Project(models.Model):
    job_title = models.ForeignKey(Job, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    proposal = models.TextField(max_length  = 500, blank=True)

    def __str__(self):
        return str(proposal)
