# Generated by Django 4.2.6 on 2023-11-09 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0003_rename_adress_hospital_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="db.department"
            ),
        ),
    ]