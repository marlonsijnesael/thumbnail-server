# Generated by Django 3.2.13 on 2022-06-08 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_rename_image_url_textureimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='textureimage',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
