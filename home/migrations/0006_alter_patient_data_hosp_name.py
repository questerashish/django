# Generated by Django 3.2 on 2021-05-11 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_patient_data_hosp_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_data',
            name='hosp_name',
            field=models.CharField(max_length=122),
        ),
    ]
