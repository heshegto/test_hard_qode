# Generated by Django 4.2.5 on 2023-09-23 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='url_adress',
            new_name='url_address',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='video_watch',
            new_name='video_watches',
        ),
    ]