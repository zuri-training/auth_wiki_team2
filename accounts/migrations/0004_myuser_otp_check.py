# Generated by Django 4.0.6 on 2022-08-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='otp_check',
            field=models.BooleanField(default=False),
        ),
    ]