# Generated by Django 3.1 on 2022-12-01 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20221126_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.payment'),
        ),
    ]