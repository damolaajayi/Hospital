# Generated by Django 2.1rc1 on 2018-10-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20181024_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Patient_Address',
            field=models.TextField(max_length=100),
        ),
    ]