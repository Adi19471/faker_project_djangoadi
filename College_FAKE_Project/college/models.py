from django.db import models

# Create your models here.



class CollegeDate(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    mobile = models.BigIntegerField()
    email  = models.EmailField()
    college = models.CharField(max_length=250)
    city = models.CharField(max_length=120)
    fees = models.FloatField()
    addmision_numbers = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.username
   
