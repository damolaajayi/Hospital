# Generated by Django 2.1rc1 on 2018-10-08 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('Reg_No', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=25)),
                ('Last_name', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=50)),
                ('Patient_Age', models.CharField(max_length=10)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('Patient_Address', models.TextField(max_length=200)),
                ('Contact_No', models.SmallIntegerField()),
                ('Room_No', models.SmallIntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Complaint', models.TextField(max_length=300)),
                ('Prescription', models.TextField(max_length=200)),
                ('Remarks', models.TextField(max_length=200)),
                ('Date', models.DateTimeField(verbose_name='Date prescribed')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
            options={
                'ordering': ('patient',),
            },
        ),
    ]
