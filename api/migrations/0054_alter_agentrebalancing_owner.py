# Generated by Django 4.1.6 on 2023-05-14 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0053_agentrebalancing_owner_addedtoapprovedrebalancing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentrebalancing',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_rebalancing', to=settings.AUTH_USER_MODEL),
        ),
    ]