# Generated by Django 4.0.4 on 2022-11-10 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_record_sensor_delete_test_record_sensor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
