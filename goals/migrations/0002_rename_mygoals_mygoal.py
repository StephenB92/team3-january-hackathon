# Generated by Django 3.2 on 2023-01-22 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyGoals',
            new_name='MyGoal',
        ),
    ]
