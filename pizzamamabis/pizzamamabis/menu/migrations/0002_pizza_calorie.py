# Generated by Django 4.1.3 on 2022-11-27 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='calorie',
            field=models.IntegerField(default=0),
        ),
    ]
