# Generated by Django 4.2 on 2023-08-30 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_message_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='score',
        ),
    ]
