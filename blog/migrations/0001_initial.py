# Generated by Django 3.2 on 2021-05-26 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=250)),
                ('articlk_info', models.CharField(max_length=250)),
                ('article_link', models.URLField()),
            ],
        ),
    ]