# Generated by Django 3.2 on 2022-06-08 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_profile_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id_user',
            field=models.PositiveIntegerField(default=0),
        ),
    ]