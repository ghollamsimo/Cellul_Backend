# Generated by Django 5.0.6 on 2024-05-22 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='appointment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.appointment'),
            preserve_default=False,
        ),
    ]
