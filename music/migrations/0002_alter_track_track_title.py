# Generated by Django 4.2.3 on 2023-07-04 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='track_title',
            field=models.CharField(max_length=30),
        ),
    ]
