# Generated by Django 5.0.1 on 2024-02-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_eventmodel_capacity_eventmodel_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='capacity',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
