# Generated by Django 2.2.17 on 2021-02-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=30),
        ),
    ]
