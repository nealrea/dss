# Generated by Django 2.1.4 on 2018-12-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20181205_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='prof_pic_num',
            field=models.IntegerField(default=6),
        ),
    ]
