# Generated by Django 4.1.7 on 2023-09-08 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apistart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmanaccount',
            name='errors',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
