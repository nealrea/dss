# Generated by Django 2.1.3 on 2018-12-12 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20181212_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='prof_pic_num',
            field=models.IntegerField(default=None, null=True),
        ),
    ]