# Generated by Django 4.0 on 2021-12-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_reciter_alter_surah_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciter',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='surah',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]