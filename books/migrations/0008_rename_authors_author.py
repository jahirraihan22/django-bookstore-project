# Generated by Django 3.2.5 on 2021-07-07 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20210707_0716'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
    ]
