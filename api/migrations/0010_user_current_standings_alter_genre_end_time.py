# Generated by Django 4.1.7 on 2023-03-16 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='current_standings',
            field=models.TextField(default='{}', max_length=400, verbose_name='Standings in different rounds'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='end_time',
            field=models.DateTimeField(verbose_name='End time of the theme: '),
        ),
    ]
