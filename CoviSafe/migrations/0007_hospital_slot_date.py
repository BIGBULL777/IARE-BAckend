# Generated by Django 3.2.8 on 2021-12-18 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoviSafe', '0006_self_assesment_test_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='slot_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]