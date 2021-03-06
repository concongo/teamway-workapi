# Generated by Django 3.2.9 on 2021-11-26 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_hour', models.IntegerField(default=0)),
                ('end_hour', models.IntegerField(default=8)),
            ],
            options={
                'verbose_name': 'Shift',
                'verbose_name_plural': 'Shifts',
                'unique_together': {('start_hour', 'end_hour')},
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('personal_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=245)),
                ('phone_number', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Worker',
                'verbose_name_plural': 'Workers',
            },
        ),
        migrations.CreateModel(
            name='WorkPlanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_shift', to='workapi.shift')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_worker', to='workapi.worker')),
            ],
            options={
                'verbose_name': 'Work Planner',
                'verbose_name_plural': 'Work Planner',
                'unique_together': {('date', 'shift', 'worker')},
            },
        ),
    ]
