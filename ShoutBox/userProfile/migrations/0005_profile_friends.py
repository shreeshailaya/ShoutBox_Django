# Generated by Django 3.2.3 on 2022-04-05 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0004_friendrequest_accepted_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='userProfile.Profile'),
        ),
    ]