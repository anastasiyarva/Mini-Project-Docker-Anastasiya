# Generated by Django 5.1.4 on 2024-12-10 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nastya_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='level',
            field=models.PositiveIntegerField(default=1, max_length=5),
        ),
    ]