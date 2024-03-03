# Generated by Django 5.0.2 on 2024-03-03 21:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanager', '0004_rename_distriute_distribute'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='distribute',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='distribute', to=settings.AUTH_USER_MODEL),
        ),
    ]