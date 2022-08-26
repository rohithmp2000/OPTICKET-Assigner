# Generated by Django 3.1.1 on 2021-04-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_tbl_patient_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_diagnosis',
            name='status',
            field=models.CharField(default='active', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbl_medicine',
            name='status',
            field=models.CharField(default='active', max_length=50),
            preserve_default=False,
        ),
    ]