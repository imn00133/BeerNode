# Generated by Django 3.1.5 on 2021-03-18 05:16

import django.core.validators
from django.db import migrations, models

import default_image


class Migration(migrations.Migration):

    dependencies = [
        ('scrapapp', '0013_auto_20210312_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrap',
            name='bitter',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='scrap',
            name='fruity',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='scrap',
            name='hoppy',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='scrap',
            name='malty',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='scrap',
            name='picture',
            field=default_image.fields.DefaultStaticImageField(blank=True, null=True, upload_to='scrap/', verbose_name='사진'),
        ),
        migrations.AlterField(
            model_name='scrap',
            name='sour',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='scrap',
            name='sweet',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
