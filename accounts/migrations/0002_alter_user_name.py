# Generated by Django 4.0 on 2021-12-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='کاربر', max_length=30, null=True),
        ),
    ]
