# Generated by Django 4.2.7 on 2024-03-25 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0014_delete_tbl_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_status', models.CharField(default=0, max_length=10)),
                ('requested_date', models.DateField(auto_now_add=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_donateform')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_patient')),
            ],
        ),
    ]