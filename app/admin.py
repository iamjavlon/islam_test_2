from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import User
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Register your models here.
from .models import User, Surah, Reciter


class FolderImportForm(forms.Form):
    folder_upload = forms.FileField()


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name',
                    'username', 'phone_number', 'date_joined']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path('upload_folder/', self.admin_site.admin_view(self.upload_folder))]
        return new_urls + urls

    def upload_folder(self, request):

        if request.method == "POST":
            csv_file = request.FILES["folder_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = User.objects.update_or_create(
                    name = fields[0],
                    balance = fields[1],
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = FolderImportForm()
        data = {"form": form}
        return render(request, "admin/folder_upload.html", data)



    admin.site.index_title = "Quran Bot"
    admin.site.site_header = "Quran Bot Admin"
    admin.site.site_title = "Admin"
    
    
admin.site.register(User, UserAdmin)
admin.site.register(Surah)
admin.site.register(Reciter)
