# Generated by Django 3.1 on 2022-11-05 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='company_name',
        ),
    ]
