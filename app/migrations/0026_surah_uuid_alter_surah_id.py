# Generated by Django 4.0 on 2022-01-16 15:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_reciter_options_alter_surah_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='surah',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='surah',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
