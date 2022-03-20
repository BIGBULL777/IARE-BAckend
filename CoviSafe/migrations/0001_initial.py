# Generated by Django 3.2.7 on 2021-12-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='citizen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=30)),
                ('last_name', models.TextField(max_length=30)),
                ('username', models.TextField(max_length=40)),
                ('age', models.IntegerField(max_length=3)),
                ('phone_number', models.IntegerField(max_length=10, unique=True)),
                ('aadhar', models.IntegerField(max_length=12)),
                ('blood_group', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.TextField(max_length=30)),
                ('test_taken', models.BooleanField(default=True)),
                ('address', models.TextField(max_length=30)),
                ('hospital_phone', models.IntegerField(max_length=12)),
                ('hospital_email', models.CharField(max_length=30)),
                ('oxygen', models.BooleanField(default=True)),
                ('blood', models.BooleanField(default=True)),
                ('total_beds', models.IntegerField()),
                ('cosultation_avail', models.BooleanField()),
                ('fees', models.IntegerField()),
            ],
        ),
    ]
