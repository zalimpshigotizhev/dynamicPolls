# Generated by Django 4.2.6 on 2024-02-04 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_remove_question_count_passes'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='respondents_count',
            field=models.IntegerField(default=0, verbose_name='Количество ответивших'),
        ),
    ]
