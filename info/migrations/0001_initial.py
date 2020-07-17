# Generated by Django 3.0.7 on 2020-06-26 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200)),
                ('institution', models.CharField(max_length=200)),
                ('start', models.CharField(max_length=10)),
                ('present', models.BooleanField(blank=True, default=False, null=True)),
                ('end', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]