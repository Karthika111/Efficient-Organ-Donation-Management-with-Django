# Generated by Django 5.0.1 on 2024-03-11 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_tbl_notification'),
        ('User', '0004_tbl_patient'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_organs',
        ),
        migrations.RemoveField(
            model_name='tbl_patient',
            name='patient_neededorgan',
        ),
        migrations.AddField(
            model_name='tbl_patient',
            name='organdata',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_organ'),
        ),
        migrations.AlterField(
            model_name='tbl_patient',
            name='patient_bloodgroup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_bloodgroup'),
        ),
    ]
