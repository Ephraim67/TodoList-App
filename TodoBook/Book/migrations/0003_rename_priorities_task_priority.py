# Generated by Django 5.0.4 on 2024-04-27 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_remove_task_priority_task_name_task_priorities'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='priorities',
            new_name='priority',
        ),
    ]
