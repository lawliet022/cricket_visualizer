# Generated by Django 3.0 on 2019-12-08 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchdata',
            name='outcome',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]