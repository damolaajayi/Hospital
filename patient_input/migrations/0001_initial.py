# Generated by Django 2.1rc1 on 2018-10-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorInfo',
            fields=[
                ('Name', models.CharField(max_length=100)),
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Age', models.CharField(max_length=50)),
                ('Contact_No', models.IntegerField()),
                ('Room', models.IntegerField()),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('Department', models.CharField(max_length=100)),
            ],
        ),
    ]
