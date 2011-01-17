from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.name