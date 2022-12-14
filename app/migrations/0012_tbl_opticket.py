# Generated by Django 3.1.5 on 2021-04-01 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_tbl_opdays_dept_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_opticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.CharField(max_length=30)),
                ('op_id', models.CharField(max_length=40)),
                ('patient_id', models.CharField(max_length=30)),
                ('dept_id', models.CharField(max_length=30)),
                ('opday', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
                ('time', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_opticket',
            },
        ),
    ]
