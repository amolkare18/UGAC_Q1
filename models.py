from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BOOKLET(models.Model):
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='BOOKLETS/')
    upload_date = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.title    
