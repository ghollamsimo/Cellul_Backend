# Generated by Django 5.0.6 on 2024-05-16 18:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_notification_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='advise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.advise'),
        ),
    ]