# Generated by Django 3.2.6 on 2021-08-28 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='slug',
        ),
    ]
