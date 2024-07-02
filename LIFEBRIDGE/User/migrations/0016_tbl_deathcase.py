# Generated by Django 4.2.7 on 2024-03-25 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0015_tbl_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_deathcase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('death_certificate', models.FileField(upload_to='CasesDocs/')),
                ('nominee_name', models.CharField(max_length=50)),
                ('case_status', models.CharField(default=0, max_length=10)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_donateform')),
            ],
        ),
    ]
