# Generated by Django 4.2 on 2025-03-21 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='typ',
            field=models.CharField(default='actio', max_length=100),
        ),
    ]
