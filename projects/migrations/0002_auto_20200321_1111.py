# Generated by Django 3.0.4 on 2020-03-21 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
