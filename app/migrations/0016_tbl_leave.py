# Generated by Django 3.1.5 on 2021-04-05 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_tbl_medicine'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=40)),
                ('days', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_leave',
            },
        ),
    ]
