# Generated by Django 5.0.6 on 2024-05-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='user',
            table='website_user',
        ),
    ]
