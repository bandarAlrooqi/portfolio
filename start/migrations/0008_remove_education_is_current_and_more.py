# Generated by Django 4.1.4 on 2022-12-17 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0007_rename_achievements_achievement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='is_current',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='is_current',
        ),
        migrations.RemoveField(
            model_name='project',
            name='is_current',
        ),
        migrations.AddField(
            model_name='achievement',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
