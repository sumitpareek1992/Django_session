# Generated by Django 3.0.8 on 2020-10-28 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201028_0850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='s_id',
        ),
    ]