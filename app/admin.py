from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms

# Register your models here.
from .models import User, Surah, Reciter


class FolderImportForm(forms.Form):
    folder_upload = forms.FileField()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name',
                    'username', 'phone_number', 'date_joined']


admin.site.register(Reciter)


@admin.register(Surah)
class SurahAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'name', 'reciter']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-folder/', self.upload_folder), ]
        return new_urls + urls

    def upload_folder(self, request):

        if request.method == "POST":
            folder = request.FILES["folder_upload"]

        form = FolderImportForm()
        data = {"form": form}
        return render(request, "admin/folder_upload.html", data)


admin.site.index_title = "Quran Bot"
admin.site.site_header = "Quran Bot Admin"
admin.site.site_title = "Admin"
