from django.db import models

# Create your models here.

class ContectUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    add_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    # def __unicode__(self):
    #     return 
