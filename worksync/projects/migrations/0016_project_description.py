# Generated by Django 5.1.7 on 2025-04-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0015_rename_text_project_projectname"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
