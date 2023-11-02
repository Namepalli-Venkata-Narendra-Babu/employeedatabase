from django.db import models
class Employee(models.Model):
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Photo=models.ImageField(upload_to='images')
    Designation=models.CharField(max_length=100)
    Email_address=models.EmailField(max_length=100,unique=True)
    Phone_number=models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.First_name
