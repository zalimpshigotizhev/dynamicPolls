# Generated by Django 3.2.23 on 2024-02-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20240203_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='name',
            field=models.CharField(default=1, max_length=200, verbose_name='Название опроса'),
            preserve_default=False,
        ),
    ]
