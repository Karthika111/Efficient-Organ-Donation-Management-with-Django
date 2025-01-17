# Generated by Django 5.0.1 on 2024-03-11 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_tbl_nominee_tbl_organs_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=20)),
                ('patient_address', models.CharField(max_length=20)),
                ('patient_contact', models.CharField(max_length=20)),
                ('patient_email', models.CharField(max_length=20)),
                ('patient_gender', models.CharField(max_length=20)),
                ('patient_bloodgroup', models.CharField(max_length=20)),
                ('patient_DOB', models.CharField(max_length=20)),
                ('patient_consultinghospital', models.CharField(max_length=20)),
                ('patient_neededorgan', models.CharField(max_length=20)),
            ],
        ),
    ]
