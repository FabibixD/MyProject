# Generated by Django 2.2.6 on 2019-12-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulechange',
            name='type',
            field=models.IntegerField(choices=[(1, 'Working by your Own'), (2, 'Different Teacher'), (3, 'Exam'), (4, 'Absent'), (5, 'Different Classroom'), (6, 'Teacher Swap')]),
        ),
    ]
