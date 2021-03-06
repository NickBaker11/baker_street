# Generated by Django 3.1.2 on 2020-11-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20201109_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room_Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_players', models.CharField(choices=[(4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], max_length=2)),
                ('date', models.DateField()),
                ('time', models.TimeField(choices=[(1000, '1000'), (1130, '1130'), (1300, '1300'), (1430, '1430'), (1600, '1600'), (1730, '1730'), (1900, '1900'), (2030, '2030'), (2200, '2200')])),
            ],
        ),
    ]
