# Generated by Django 3.0.5 on 2023-07-17 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Laboratoire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratoire',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
