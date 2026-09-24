from django.db import models

# Create your models here.
class Contact(models.Model):
  id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  phone = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  
  def __str__(self):
    return self.last_name