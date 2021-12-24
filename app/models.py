from django.db import models

# Create your models here.


class User(models.Model):
    
    LANGUAGES = [
        ('uz', "O'zbek"),
        ('ru', "Русский"),
        ('en', "English")
    ]
    
    
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(
        max_length=255, null=True, blank=True)
    last_name = models.CharField(
        max_length=255, null=True, blank=True)
    username = models.CharField(
        max_length=255, null=True, blank=True)
    phone_number =  models.PositiveBigIntegerField(
        null=True, blank=True)
    language = models.CharField(
        max_length=2, choices=LANGUAGES, default=None, null=True)
    date_joined = models.DateField(
        null=True, auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
class Surah(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    audio = models.FileField(upload_to='media/')