# Generated by Django 4.1.3 on 2022-11-19 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('phone_No', models.CharField(max_length=20)),
                ('address_Details', models.JSONField(null=True)),
                ('work_Experience', models.JSONField(null=True)),
                ('qualifications', models.JSONField(null=True)),
                ('projects', models.JSONField(null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]
