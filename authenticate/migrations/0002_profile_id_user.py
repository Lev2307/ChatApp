# Generated by Django 3.2 on 2022-06-08 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id_user',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
