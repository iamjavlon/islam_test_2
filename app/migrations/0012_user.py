# Generated by Django 4.0 on 2021-12-16 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.PositiveBigIntegerField(blank=True, null=True)),
                ('language', models.CharField(choices=[('en', 'English'), ('ru', 'Русский')], default=None, max_length=2, null=True)),
                ('date_joined', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]