# Generated by Django 3.2.23 on 2024-02-03 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_choice_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
    ]