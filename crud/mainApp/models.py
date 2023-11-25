from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    sal = models.IntegerField()
    city = models.CharField(max_length=60,default="",null=True,blank=True)
    state = models.CharField(max_length=60,default="",null=True,blank=True)

    def __str__(self):
        return str(self.id)+" "+self.name
