# Generated by Django 5.1.7 on 2025-04-09 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0007_task_team"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="team",
            name="members",
        ),
        migrations.DeleteModel(
            name="Task",
        ),
        migrations.DeleteModel(
            name="Team",
        ),
    ]
