# Generated by Django 3.2.7 on 2021-09-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(max_length=20),
        ),
    ]