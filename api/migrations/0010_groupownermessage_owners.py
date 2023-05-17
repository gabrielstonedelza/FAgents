# Generated by Django 4.1.6 on 2023-05-17 15:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0009_ownerchat_groupownermessage_groupagentsmessage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupownermessage',
            name='owners',
            field=models.ManyToManyField(related_name='owners_chatting_with_owners', to=settings.AUTH_USER_MODEL),
        ),
    ]