# Generated by Django 2.1.7 on 2019-09-04 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20190904_0437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='business_fax',
        ),
    ]