from django.contrib import admin

# Register your models here.
from .models import User, Surah, Reciter

admin.site.register(User)
admin.site.register(Surah)
admin.site.register(Reciter)