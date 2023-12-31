# Generated by Django 4.2.3 on 2023-07-27 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Laboratoire', '0009_alter_laboratoire_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reference', models.CharField(max_length=200, null=True, unique=True)),
                ('Etat', models.CharField(choices=[('Installé', 'Installé'), ('en panne', 'En panne'), ('Fonctionnel', 'Fonctionnel')], max_length=200, null=True)),
                ('Date_Acquisition', models.DateField(auto_now_add=True)),
                ('Marque', models.CharField(max_length=200, null=True)),
                ('Categorie', models.CharField(choices=[('Chimie', 'Chimie'), ('Biologie', 'Biologie'), ('Microbiologie', 'Microbiologie'), ('Biotechnologie', 'Biotechnologie'), ('Autre', 'Autre')], max_length=200)),
                ('Laboratoire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Laboratoire.laboratoire')),
            ],
        ),
    ]
