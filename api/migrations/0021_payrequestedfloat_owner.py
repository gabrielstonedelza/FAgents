# Generated by Django 4.1.6 on 2024-01-25 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0020_alter_requestfloat_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='payrequestedfloat',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owner_receiving_payments', to=settings.AUTH_USER_MODEL),
        ),
    ]