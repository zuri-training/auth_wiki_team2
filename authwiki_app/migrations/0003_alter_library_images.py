# Generated by Django 4.0.6 on 2022-08-04 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authwiki_app', '0002_library'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='images',
            field=models.ImageField(blank=True, upload_to='library_images'),
        ),
    ]
