# Generated by Django 3.1.5 on 2021-04-05 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_tbl_labtest'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_id', models.CharField(max_length=30)),
                ('diagnosis_id', models.CharField(max_length=40)),
                ('medicinename', models.CharField(max_length=30)),
                ('dosage', models.CharField(max_length=30)),
                ('rate', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'tbl_medicine',
            },
        ),
    ]
