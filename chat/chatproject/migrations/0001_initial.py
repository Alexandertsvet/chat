# Generated by Django 5.0.6 on 2024-05-18 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название группы', max_length=200, verbose_name='название')),
                ('slug', models.SlugField(help_text='Введите уникальный фрагмент URL-адреса для группы', unique=True, verbose_name='уникальный фрагмент URL-адреса')),
                ('description', models.TextField(help_text='Введите описание группы', verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'група',
                'verbose_name_plural': 'Группы',
            },
        ),
    ]