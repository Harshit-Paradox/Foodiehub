# Generated by Django 5.0.7 on 2024-08-08 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_profile_contact_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="address",
            field=models.TextField(blank=True),
        ),
    ]
