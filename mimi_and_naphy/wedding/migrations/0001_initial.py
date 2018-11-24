# Generated by Django 2.1.3 on 2018-11-10 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=255)),
                ('image', models.FileField(null=True, upload_to='wedding/%Y/%m/%d/')),
                ('description', models.TextField()),
                ('priority', models.IntegerField()),
            ],
            options={
                'ordering': ['priority'],
            },
        ),
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number_of_attendees', models.IntegerField()),
                ('phone_number', models.CharField(max_length=255)),
                ('attending', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]