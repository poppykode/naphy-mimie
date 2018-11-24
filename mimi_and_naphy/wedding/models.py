from django.db import models
from django.urls import reverse

# Create your models here.

class Gallery(models.Model):
  
    caption = models.CharField(max_length=255)
    image = models.FileField(upload_to='wedding/%Y/%m/%d/',null=True, blank =False,)
    description =  models.TextField()
    priority = models.IntegerField()

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ['priority']

class RSVP(models.Model):

    ATTENDANCE =(
        ('Attending','Attending'),
        ('Not Attending','Not Attending'),
        ('Mybe','Mybe'),
    )
    name = models.CharField(max_length=255)
    number_of_attendees =  models.IntegerField()
    phone_number = models.CharField(max_length=255)
    holy_metromony = models.CharField(max_length=100, choices=ATTENDANCE,default='Attending', blank = False)
    wedding_party = models.CharField(max_length=100, choices=ATTENDANCE,default='Attending', blank = False)
    message = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wedding:rsvp")

class BridalTeam(models.Model):
  
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='team/%Y/%m/%d/',null=True, blank =False,)
    facebook_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100,null=True, blank =False)
    email = models.EmailField()
    phone = models.CharField(max_length=100,null=True, blank =False)
    message = models.TextField(null=True)

    def __str__ (self):
        return self.name
        
    def get_absolute_url(self):
        return reverse("wedding:contact")


    


