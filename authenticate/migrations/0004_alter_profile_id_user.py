# Generated by Django 3.2 on 2022-06-09 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_alter_profile_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id_user',
            field=models.PositiveIntegerField(default=1),
        ),
    ]