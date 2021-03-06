# Generated by Django 2.2.5 on 2020-01-11 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_remove_schedulechange_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulechange',
            name='absent_from',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedulechange',
            name='absent_to',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedulechange',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Teacher'),
        ),
        migrations.AlterField(
            model_name='schedulechange',
            name='type',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
