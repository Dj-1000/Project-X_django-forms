from django.db import models
from django.contrib.auth.models import User
class Record(models.Model):
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add = True)
    first_name = models.CharField(max_length =50)
    last_name = models.CharField(max_length =50)
    email = models.EmailField(max_length =100)
    phone = models.CharField(max_length = 12)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length = 50)
   
    
    def __str__(self):
        return self.first_name+" " +self.last_name
    
    
