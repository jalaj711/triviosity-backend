# Generated by Django 4.0.6 on 2022-07-15 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('text', models.TextField()),
                ('round', models.IntegerField(primary_key=True, serialize=False)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.TextField(serialize=False, unique=True)),
                ('password', models.TextField()),
                ('salt', models.TextField()),
                ('points', models.IntegerField(default=0)),
                ('current_round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_round', to='api.question')),
            ],
        ),
        migrations.CreateModel(
            name='Clues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='api.question')),
            ],
        ),
        migrations.CreateModel(
            name='AccessTokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
                ('expires_on', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='api.user')),
            ],
        ),
    ]