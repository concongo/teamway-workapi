# Generated by Django 3.2.9 on 2021-11-27 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workapi', '0002_rename_lastname_worker_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workplanner',
            name='shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_plan', to='workapi.shift'),
        ),
        migrations.AlterField(
            model_name='workplanner',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_plan', to='workapi.worker'),
        ),
    ]