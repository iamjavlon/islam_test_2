# Generated by Django 4.0 on 2022-01-16 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_user_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reciter',
            options={'verbose_name': 'Reciter', 'verbose_name_plural': 'Reciters'},
        ),
        migrations.AlterModelOptions(
            name='surah',
            options={'verbose_name': 'Surah', 'verbose_name_plural': 'Surahs'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
