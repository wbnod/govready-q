# Generated by Django 2.0.13 on 2019-07-17 20:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0027_auto_20190708_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='projects',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolio',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='portfolio',
            field=models.ForeignKey(blank=True, help_text='The Portfolio that this Project belongs to.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='siteapp.Portfolio'),
        ),
    ]