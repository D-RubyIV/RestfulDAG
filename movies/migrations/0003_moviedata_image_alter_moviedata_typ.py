# Generated by Django 4.2 on 2025-03-21 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='Images/None/Noimg.jpg', upload_to='Images/'),
        ),
        migrations.AlterField(
            model_name='moviedata',
            name='typ',
            field=models.CharField(default='action', max_length=100),
        ),
    ]
