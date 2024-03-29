# Generated by Django 3.2.23 on 2024-02-03 11:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20240203_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.poll', verbose_name='Если вариант отвечает на вопрос'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
    ]
