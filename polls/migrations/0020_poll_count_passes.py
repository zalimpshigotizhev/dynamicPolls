# Generated by Django 4.2.6 on 2024-02-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_poll_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='count_passes',
            field=models.IntegerField(default=0, verbose_name='Количество проходов'),
        ),
    ]
