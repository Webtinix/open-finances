# Generated by Django 5.0 on 2024-01-25 17:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bordereaulivraison',
            options={'verbose_name': 'Bordereau de livraison', 'verbose_name_plural': 'Bordereaux de livraison'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='facture',
            options={'verbose_name': 'Facture', 'verbose_name_plural': 'Factures'},
        ),
        migrations.AlterModelOptions(
            name='rapport',
            options={'verbose_name': 'Rapport', 'verbose_name_plural': 'Rapports'},
        ),
        migrations.AlterField(
            model_name='bordereaulivraison',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Créateur'),
        ),
        migrations.AlterField(
            model_name='bordereaulivraison',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='bordereaulivraison',
            name='date_livraison',
            field=models.DateField(verbose_name='Date de livraison'),
        ),
        migrations.AlterField(
            model_name='bordereaulivraison',
            name='date_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification'),
        ),
        migrations.AlterField(
            model_name='bordereaulivraison',
            name='facture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.facture', verbose_name='Facture'),
        ),
        migrations.AlterField(
            model_name='bordereaulivraison',
            name='numero_bl',
            field=models.CharField(max_length=100, verbose_name='Numéro du bordereau'),
        ),
        migrations.AlterField(
            model_name='client',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Créateur'),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification'),
        ),
        migrations.AlterField(
            model_name='client',
            name='denomination',
            field=models.CharField(max_length=100, verbose_name='Dénomination'),
        ),
        migrations.AlterField(
            model_name='client',
            name='numero_enreg',
            field=models.CharField(max_length=100, verbose_name="Numéro d'enregistrement"),
        ),
        migrations.AlterField(
            model_name='client',
            name='signe',
            field=models.CharField(max_length=100, verbose_name='Signe'),
        ),
        migrations.AlterField(
            model_name='facture',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.client', verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='facture',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Créateur'),
        ),
        migrations.AlterField(
            model_name='facture',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='facture',
            name='date_facture',
            field=models.DateField(verbose_name='Date de la facture'),
        ),
        migrations.AlterField(
            model_name='facture',
            name='date_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification'),
        ),
        migrations.AlterField(
            model_name='facture',
            name='montant_total',
            field=models.IntegerField(verbose_name='Montant total'),
        ),
        migrations.AlterField(
            model_name='facture',
            name='numero_ordre',
            field=models.CharField(max_length=100, verbose_name="Numéro d'ordre"),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='date_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='facture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.facture', verbose_name='Facture'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='nombre_bouteilles',
            field=models.IntegerField(default=0, verbose_name='Nombre de bouteilles'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='poids_bouteilles',
            field=models.IntegerField(default=0, verbose_name='Poids de bouteilles'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='total_par_categories',
            field=models.IntegerField(default=0, verbose_name='Total par catégories'),
        ),
    ]
