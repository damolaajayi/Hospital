# Generated by Django 2.1rc1 on 2018-10-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_input', '0002_auto_20181022_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorinfo',
            name='Contact_No',
            field=models.IntegerField(max_length=50),
        ),
    ]
