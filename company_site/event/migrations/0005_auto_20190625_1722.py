# Generated by Django 2.2.2 on 2019-06-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20190625_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_heading',
            field=models.CharField(max_length=20),
        ),
    ]