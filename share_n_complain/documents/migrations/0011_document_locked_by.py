# Generated by Django 2.1.3 on 2018-12-04 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0010_document_locked'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='locked_by',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]