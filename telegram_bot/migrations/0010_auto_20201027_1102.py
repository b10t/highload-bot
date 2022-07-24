# Generated by Django 3.1.2 on 2020-10-27 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0009_auto_20201027_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollquestionanswerpair',
            name='slug',
            field=models.SlugField(null=True, verbose_name='Slug вопроса'),
        ),
        migrations.AlterField(
            model_name='pollquestionanswerpair',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='poll_question_answer_pairs', to='telegram_bot.pollresult', verbose_name='Опрос'),
        ),
    ]