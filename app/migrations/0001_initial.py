# Generated by Django 4.0 on 2021-12-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='Title of the product')),
                ('description', models.TextField(default='This is description of this product')),
                ('price', models.TextField(default='9.99')),
                ('summary', models.TextField(default='this is cool!')),
            ],
        ),
    ]
