# Generated by Django 3.2.13 on 2022-06-19 16:04

from django.db import migrations, models
import project.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_alter_project_scene'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='scene',
            field=models.FileField(upload_to=project.models.scene_upload_to),
        ),
    ]
