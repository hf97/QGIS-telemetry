# Generated by Django 3.1.6 on 2021-06-17 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='added_layer',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='added_layer',
            name='telemetry',
        ),
        migrations.RemoveField(
            model_name='server',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='server',
            name='location',
        ),
        migrations.AddField(
            model_name='action',
            name='added_layer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='server.added_layer'),
        ),
        migrations.DeleteModel(
            name='Provider',
        ),
    ]