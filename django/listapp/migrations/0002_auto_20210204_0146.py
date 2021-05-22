# Generated by Django 3.1.5 on 2021-02-03 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scraplist',
            name='image',
            field=models.ImageField(null=True, upload_to='scraplist/'),
        ),
        migrations.AddField(
            model_name='scraplist',
            name='message',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='scraplist',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='scraplist', to=settings.AUTH_USER_MODEL),
        ),
    ]