# Generated by Django 5.0.1 on 2024-04-17 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0009_alter_tbl_hospital_hospital_logo_and_more'),
        ('User', '0017_tbl_feedback_tbl_complaint'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tbl_complaint',
            new_name='tbl_complaints',
        ),
    ]
