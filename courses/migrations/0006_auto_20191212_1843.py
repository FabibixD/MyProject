# Generated by Django 2.2.5 on 2019-12-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20191212_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulechange',
            name='degree',
            field=models.IntegerField(blank=True, choices=[(1, '5a'), (2, '5b'), (3, '5c'), (4, '5d'), (5, '6a'), (6, '6b'), (7, '6c'), (8, '6d'), (9, '7a'), (10, '7b'), (11, '7c'), (12, '7d'), (13, '8a'), (14, '8b'), (15, '8c'), (16, '9a'), (17, '9b'), (18, '9c'), (19, '9d'), (20, 'AG'), (21, 'EF'), (22, 'Q1'), (23, 'Q2')], default=1),
        ),
    ]
