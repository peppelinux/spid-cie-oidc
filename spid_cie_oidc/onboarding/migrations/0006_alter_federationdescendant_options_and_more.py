# Generated by Django 4.0.2 on 2022-02-05 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_onboarding', '0005_alter_federationdescendant_jwks_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='federationdescendant',
            options={'verbose_name': 'Federation Entity Descendant', 'verbose_name_plural': 'Federation Entity Descendants'},
        ),
        migrations.AlterModelOptions(
            name='federationdescendantcontact',
            options={'verbose_name': 'Federation Entity Contact', 'verbose_name_plural': 'Federation Entity Contacts'},
        ),
    ]
