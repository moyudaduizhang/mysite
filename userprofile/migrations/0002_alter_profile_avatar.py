# Generated by Django 5.0.4 on 2024-05-09 10:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userprofile", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(blank=True, upload_to="avatar/%y%m%d"),
        ),
    ]
