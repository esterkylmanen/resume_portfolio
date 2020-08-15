from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.BigIntegerField()
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=50)
    github = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        self.github = self.github.lower()
        self.linkedin = self.linkedin.lower()
        return super(Contact, self).save(*args, **kwargs)
    
    def __str__(self):
        name = self.first_name + " " + self.last_name
        return name
    

class Skill(models.Model):
    class Scale(models.IntegerChoices):
        
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    
    title = models.CharField(max_length=50)
    scale = models.IntegerField(choices=Scale.choices)
    
    def __str__(self):
        return self.title
    

class Experience(models.Model):
    title = models.CharField(max_length=60)
    employer = models.CharField(max_length=50)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
    
class Education(models.Model):
    title = models.CharField(max_length=60)
    school = models.CharField(max_length=50)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    