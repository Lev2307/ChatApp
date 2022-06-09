# Generated by Django 3.2 on 2022-06-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='message',
        ),
        migrations.AddField(
            model_name='chat',
            name='room_id',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
