# Generated by Django 4.1.6 on 2023-07-21 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_agentandowneraccounts_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentandowneraccounts',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
