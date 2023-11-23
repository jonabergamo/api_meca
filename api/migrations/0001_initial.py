# Generated by Django 4.2.7 on 2023-11-17 00:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IncubatorSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('incubation_duration', models.DurationField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IncubatorDevice',
            fields=[
                ('unique_id', models.CharField(default='b79200d4-133e-4dc9-8912-1000e85fbf36', editable=False, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('is_on', models.BooleanField(default=False)),
                ('humidity_sensor', models.CharField(max_length=100)),
                ('temperature_sensor', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('current_setting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_devices', to='api.incubatorsetting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
