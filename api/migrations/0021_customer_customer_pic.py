# Generated by Django 4.1.6 on 2023-05-03 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_agentaccountsbalancestarted_time_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_pic',
            field=models.ImageField(default='', upload_to='customer_pics'),
        ),
    ]