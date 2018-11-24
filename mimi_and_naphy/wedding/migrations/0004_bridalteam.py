# Generated by Django 2.1.3 on 2018-11-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0003_auto_20181110_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='BridalTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.FileField(null=True, upload_to='team/%Y/%m/%d/')),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
