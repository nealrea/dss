# Generated by Django 2.1.3 on 2018-11-24 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
