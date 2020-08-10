from django.db import models

class Skill(models.Model):
    class Scale(models.IntegerChoices):
        
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    
    title = models.CharField(max_length=50)
    scale = models.IntegerField(choices=Scale.choices)
    

class Experience(models.Model):
    title = models.CharField(max_length=50)
    employer = models.CharField(max_length=50)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=True, auto_now_add=False)
    description = models.CharField(max_length=100)
    
    
class Education(models.Model):
    title = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=True, auto_now_add=False)
    description = models.CharField(max_length=100)