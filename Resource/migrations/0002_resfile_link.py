# Generated by Django 2.1.7 on 2019-04-11 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resfile',
            name='link',
            field=models.CharField(default='', max_length=1000),
        ),
    ]