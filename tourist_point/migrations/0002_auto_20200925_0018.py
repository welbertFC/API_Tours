# Generated by Django 3.1.1 on 2020-09-25 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_point', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristpoint',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]