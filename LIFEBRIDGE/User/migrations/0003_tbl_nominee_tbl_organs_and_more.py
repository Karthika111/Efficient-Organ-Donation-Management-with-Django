# Generated by Django 5.0.1 on 2024-03-11 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_tbl_user_delete_tbl_donateform'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_nominee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominee_name', models.CharField(max_length=20)),
                ('nominee_relation', models.CharField(max_length=20)),
                ('nominee_email', models.CharField(max_length=20)),
                ('nominee_proof', models.FileField(upload_to='nominee/')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_organs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organ_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='tbl_user',
            new_name='tbl_donateform',
        ),
    ]