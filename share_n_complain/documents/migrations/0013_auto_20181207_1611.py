# Generated by Django 2.1.3 on 2018-12-07 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0012_document_taboo_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='private',
            field=models.BooleanField(default=False, verbose_name='Private?'),
        ),
    ]
