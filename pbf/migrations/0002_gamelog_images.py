# Generated by Django 4.0.1 on 2022-02-03 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamelog',
            name='images',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
