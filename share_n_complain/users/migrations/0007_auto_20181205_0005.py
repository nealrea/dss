# Generated by Django 2.1.4 on 2018-12-05 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_prof_pic_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='prof_pic_num',
            field=models.IntegerField(default=4),
        ),
    ]