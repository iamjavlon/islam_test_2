from enum import unique
from django.db import models

# Create your models here.


class User(models.Model):

    LANGUAGES = [
        ('uz', "O'zbek"),
        ('ru', "Русский"),
        ('en', "English")
    ]

    id = models.BigIntegerField(primary_key=True, editable=False)
    first_name = models.CharField(
        max_length=255, null=True, blank=True)
    last_name = models.CharField(
        max_length=255, null=True, blank=True)
    username = models.CharField(
        max_length=255, null=True, blank=True)
    phone_number = models.PositiveBigIntegerField(
        null=True, blank=True)
    language = models.CharField(
        max_length=2, choices=LANGUAGES, default=None, null=True)
    date_joined = models.DateField(
        null=True, auto_now_add=True)

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return str(self.id)


class Reciter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=255, null=True, blank=True)
    description = models.TextField(
        null=True, blank=True)

    class Meta:
        verbose_name = ("Reciter")
        verbose_name_plural = ("Reciters")

    def __str__(self):
        return str(self.name)


class Surah(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField(null=True, blank=True)
    name = models.CharField(
        max_length=150, null=True, blank=True)
    description = models.TextField(
        null=True, blank=True, default=None)
    audio = models.FileField(
        upload_to='media/surahs/')
    reciter = models.ForeignKey(
        Reciter, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = ("Surah")
        verbose_name_plural = ("Surahs")

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=200, null=False, blank=True)
    heading = models.CharField(
        max_length=250, null=True, blank=True)
    body = models.TextField(
        null=True, blank=True, default=None)
    image_id = models.IntegerField(
        null=True, blank=True)
    media = models.ImageField(
        upload_to='media/posts/')
    date_posted = models.DateTimeField(
        auto_now_add=True)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return str(self.title)
