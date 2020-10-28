# Generated by Django 3.1.2 on 2020-10-28 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_title', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('room_description', models.CharField(max_length=254)),
                ('room_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
