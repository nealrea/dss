# Generated by Django 2.1.3 on 2018-12-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0009_history_updater_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='locked',
            field=models.BooleanField(default=False, verbose_name='Locked Status'),
        ),
    ]
