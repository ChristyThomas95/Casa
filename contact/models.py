from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    design_id = models.IntegerField()
    customer_need = models.CharField(max_length=100)
    design_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(max_length=100)
    user_id = models.IntegerField(blank=True)
    created_at = models.DateTimeField(blank=True, default=datetime.now)
    
    def __str__(self):
        return self.email