# Generated by Django 4.2.8 on 2023-12-12 19:06

from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0032_Drop_Zoom_integration"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="dashamail_list_id",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="bundle",
            name="group",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="products.group", verbose_name="Analytical group"),
        ),
        migrations.AlterField(
            model_name="course",
            name="group",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="products.group", verbose_name="Analytical group"),
        ),
        migrations.AlterField(
            model_name="record",
            name="group",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="products.group", verbose_name="Analytical group"),
        ),
    ]
