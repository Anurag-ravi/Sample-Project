# Generated by Django 3.2.4 on 2021-10-07 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumini',
            name='profile',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
