# Generated by Django 2.1rc1 on 2018-10-22 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_input', '0004_auto_20181022_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorinfo',
            name='ID',
        ),
        migrations.AddField(
            model_name='doctorinfo',
            name='id',
            field=models.AutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
