# Generated by Django 2.1.3 on 2018-11-30 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0008_auto_20181130_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='updater_ids',
            field=models.CharField(default='', max_length=100),
        ),
    ]
