# Generated by Django 4.1.1 on 2022-09-26 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_remove_video_github_link_video_author_github_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='difficult',
            field=models.CharField(choices=[(1, 'начальный уровень'), (2, 'требуется подготовка'), (3, 'для профи')], default=1, max_length=20, verbose_name='Сложность'),
        ),
    ]