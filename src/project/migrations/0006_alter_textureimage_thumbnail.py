# Generated by Django 3.2.13 on 2022-06-09 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_textureimage_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textureimage',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
