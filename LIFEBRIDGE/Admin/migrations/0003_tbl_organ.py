# Generated by Django 5.0.1 on 2024-02-13 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_tbl_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_organ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organ_name', models.CharField(max_length=20)),
            ],
        ),
    ]
