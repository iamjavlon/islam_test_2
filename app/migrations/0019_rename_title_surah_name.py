# Generated by Django 4.0 on 2021-12-26 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_user_language'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surah',
            old_name='title',
            new_name='name',
        ),
    ]