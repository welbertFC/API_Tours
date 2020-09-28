# Generated by Django 3.1.1 on 2020-09-28 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(blank=True, max_length=150, null=True)),
                ('line2', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=70)),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longitude', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
