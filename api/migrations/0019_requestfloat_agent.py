# Generated by Django 4.1.6 on 2024-01-25 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0018_requestfloat_amount_alter_requestfloat_float_request_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestfloat',
            name='agent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_requesting_for_float', to=settings.AUTH_USER_MODEL),
        ),
    ]
