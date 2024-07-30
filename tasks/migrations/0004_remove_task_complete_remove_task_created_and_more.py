# Generated by Django 5.0.6 on 2024-07-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_remove_task_category_remove_task_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='importance',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]