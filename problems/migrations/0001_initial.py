# Generated by Django 4.0 on 2021-12-13 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('creted', models.DateTimeField(auto_now_add=True)),
                ('q_head', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
