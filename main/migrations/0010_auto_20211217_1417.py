# Generated by Django 3.2.9 on 2021-12-17 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_video_date_redact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date_redact',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='date_redact',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
