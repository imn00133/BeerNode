# Generated by Django 3.1.5 on 2021-03-16 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0002_auto_20210223_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='nickname',
        ),
    ]
