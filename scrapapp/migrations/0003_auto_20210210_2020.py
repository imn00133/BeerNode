# Generated by Django 3.1.5 on 2021-02-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapapp', '0002_scrap_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrap',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='scrap/', verbose_name='사진'),
        ),
    ]