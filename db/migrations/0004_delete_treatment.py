# Generated by Django 4.2.6 on 2023-11-20 09:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0003_alter_accounting_patient"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Treatment",
        ),
    ]
