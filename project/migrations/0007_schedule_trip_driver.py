# Generated by Django 4.0.3 on 2022-05-28 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DriverName', models.CharField(default='', max_length=100)),
                ('StartTime', models.TimeField()),
                ('EndTime', models.TimeField()),
            ],
            options={
                'db_table': 'Schedules',
            },
        ),
        migrations.AddField(
            model_name='trip',
            name='Driver',
            field=models.CharField(default='', max_length=100),
        ),
    ]
