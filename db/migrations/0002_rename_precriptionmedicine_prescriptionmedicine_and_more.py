# Generated by Django 4.2.7 on 2023-11-17 06:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PrecriptionMedicine",
            new_name="PrescriptionMedicine",
        ),
        migrations.RenameField(
            model_name="prescriptionmedicine",
            old_name="precription",
            new_name="prescription",
        ),
    ]