# Generated by Django 4.0.6 on 2022-08-01 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_question_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='clues',
            name='clue_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clues',
            name='wait_time_in_minutes',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='user',
            name='calc_wait_time_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='current_clue',
            field=models.IntegerField(default=0),
        ),
    ]
