# Generated by Django 4.0.6 on 2022-08-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authwiki_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('dowload_slug', models.URLField(max_length=250)),
                ('images', models.ImageField(blank=True, upload_to='')),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]