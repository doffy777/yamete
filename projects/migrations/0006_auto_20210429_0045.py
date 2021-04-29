# Generated by Django 3.2 on 2021-04-28 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_summary'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Summary',
        ),
        migrations.AddField(
            model_name='videos',
            name='author',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='videos',
            name='genre',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='videos',
            name='release',
            field=models.TextField(blank=True, null=True),
        ),
    ]
