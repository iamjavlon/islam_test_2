from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# Register your models here.
from .models import User, Surah, Reciter


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name',
                    'username', 'phone_number', 'date_joined']
    admin.site.index_title = "Quran Bot"
    admin.site.site_header = "Quran Bot Admin"
    admin.site.site_title = "Admin"

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-folder/', self.upload_folder),]
        return new_urls + urls
    
    def upload_folder(self, request):
        return render(request, "admin/folder_upload.html")
    
    
    
admin.site.register(User, UserAdmin)
admin.site.register(Surah)
admin.site.register(Reciter)
