# Generated by Django 3.2.9 on 2021-11-27 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workapi', '0003_auto_20211127_0709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shift',
            options={'ordering': ('start_hour',), 'verbose_name': 'Shift', 'verbose_name_plural': 'Shifts'},
        ),
        migrations.AlterModelOptions(
            name='worker',
            options={'ordering': ('personal_id',), 'verbose_name': 'Worker', 'verbose_name_plural': 'Workers'},
        ),
        migrations.AlterModelOptions(
            name='workplanner',
            options={'ordering': ('date', 'shift', 'worker'), 'verbose_name': 'Work Planner', 'verbose_name_plural': 'Work Planner'},
        ),
    ]
