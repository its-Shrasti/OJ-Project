# Generated by Django 5.2.1 on 2025-05-20 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], max_length=10)),
                ('topic', models.CharField(max_length=50)),
                ('testcases', models.TextField(help_text='Store as JSON or plain text')),
                ('hints', models.TextField(blank=True, null=True)),
                ('constraints', models.TextField(blank=True, null=True)),
                ('problem_statistics', models.JSONField(blank=True, default=dict)),
                ('isSolved', models.BooleanField(default=False)),
            ],
        ),
    ]
