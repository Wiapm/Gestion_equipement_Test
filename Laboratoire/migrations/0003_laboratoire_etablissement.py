# Generated by Django 3.0.5 on 2023-07-18 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Etablissement', '0002_auto_20230717_2157'),
        ('Laboratoire', '0002_auto_20230717_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratoire',
            name='Etablissement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Etablissement.Etablissement'),
        ),
    ]
