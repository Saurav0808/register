# Generated by Django 3.2.7 on 2021-09-26 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_model',
            name='Name',
        ),
        migrations.AddField(
            model_name='register_model',
            name='Email',
            field=models.CharField(default='0000000', max_length=50),
        ),
        migrations.AddField(
            model_name='register_model',
            name='Password',
            field=models.CharField(default='0000000', max_length=50),
        ),
        migrations.AddField(
            model_name='register_model',
            name='Password2',
            field=models.CharField(default='0000000', max_length=50),
        ),
    ]
