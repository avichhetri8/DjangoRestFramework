# Generated by Django 3.0.7 on 2020-06-07 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestExample', '0003_auto_20200607_0627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='descritption',
            new_name='description',
        ),
    ]
