# Generated by Django 3.2.4 on 2022-03-03 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScLineUsr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('vk', models.CharField(max_length=30)),
                ('inst', models.CharField(max_length=30)),
                ('tiktok', models.CharField(max_length=30)),
                ('youtube', models.CharField(max_length=30)),
                ('facebook', models.CharField(max_length=30)),
                ('link1', models.CharField(max_length=30)),
                ('link2', models.CharField(max_length=30)),
                ('link3', models.CharField(max_length=30)),
                ('link4', models.CharField(max_length=30)),
                ('link5', models.CharField(max_length=30)),
            ],
        ),
    ]
