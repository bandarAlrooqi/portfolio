# Generated by Django 4.1.4 on 2022-12-16 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0003_alter_projects_description_alter_projects_from_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]