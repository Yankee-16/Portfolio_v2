# Generated by Django 3.0.7 on 2020-06-26 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]