# Generated by Django 5.0.6 on 2024-05-12 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Advise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now=True)),
                ('localisation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Student', 'Student'), ('Advise', 'Advise')], max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('date', models.DateField()),
                ('advise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.advise')),
            ],
        ),
        migrations.CreateModel(
            name='Collaboration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('university', models.CharField(max_length=200)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.admin')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=200)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.event')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('advise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.advise')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.event')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.student')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(max_length=255)),
                ('shared', models.BooleanField(default=False)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.user'),
        ),
        migrations.AddField(
            model_name='advise',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.user'),
        ),
        migrations.AddField(
            model_name='admin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.user'),
        ),
    ]
