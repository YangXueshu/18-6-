from django.db import models

# Create your models here.
class S_CURRICULUM(models.Model):
    name = models.CharField(max_length=200)
    week_day = models.IntegerField(default=0)
    time_begin = models.TimeField() 
    time_end = models.TimeField()
    def __str__(self):
        return self.name

class Students(models.Model):
    name = models.CharField(max_length=200)
    s_class = models.IntegerField(default=0)
    s_id = models.CharField(max_length=200)
    s_grade = models.CharField(max_length=100)
    s_photo = models.ImageField(upload_to='cover/')  
    s_curriculum = models.ManyToManyField(S_CURRICULUM)
    s_time = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class Sign(models.Model):
    name = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    def __str__(self):
        return self.name