# Generated by Django 3.2.7 on 2021-12-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoviSafe', '0002_auto_20211218_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='isolation',
            field=models.BooleanField(default=False),
        ),
    ]
