# Generated by Django 5.0.6 on 2024-07-30 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_remove_task_complete_remove_task_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]