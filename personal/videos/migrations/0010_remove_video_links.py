# Generated by Django 4.1.1 on 2022-09-26 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_delete_category_alter_video_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='links',
        ),
    ]
