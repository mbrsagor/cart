# Generated by Django 3.1.4 on 2020-12-15 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20201215_0827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Library',
            new_name='library',
        ),
    ]
