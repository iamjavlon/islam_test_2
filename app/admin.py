from django.contrib import admin

# Register your models here.
from .models import User, Surah, Reciter


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name',
                    'username', 'phone_number', 'date_joined']


admin.site.register(User, UserAdmin)
admin.site.register(Surah)
admin.site.register(Reciter)
