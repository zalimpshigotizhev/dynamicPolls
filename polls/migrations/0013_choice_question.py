# Generated by Django 3.2.23 on 2024-02-03 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20240203_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.question', verbose_name='Если вариант отвечает на вопрос'),
            preserve_default=False,
        ),
    ]
