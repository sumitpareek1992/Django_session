# Generated by Django 3.0.8 on 2020-11-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20201102_0642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='collage_id',
        ),
        migrations.AlterField(
            model_name='students',
            name='s_id',
            field=models.CharField(max_length=10),
        ),
    ]