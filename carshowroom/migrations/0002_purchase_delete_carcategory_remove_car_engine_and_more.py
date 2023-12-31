# Generated by Django 4.2.3 on 2023-07-30 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("carshowroom", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Purchase",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("purchase_date", models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name="CarCategory",
        ),
        migrations.RemoveField(
            model_name="car",
            name="engine",
        ),
        migrations.RemoveField(
            model_name="car",
            name="features",
        ),
        migrations.RemoveField(
            model_name="car",
            name="owner",
        ),
        migrations.RemoveField(
            model_name="feature",
            name="model",
        ),
        migrations.AddField(
            model_name="customer",
            name="showroom",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="carshowroom.showroom",
            ),
        ),
        migrations.AddField(
            model_name="purchase",
            name="car",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="carshowroom.car"
            ),
        ),
        migrations.AddField(
            model_name="purchase",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="carshowroom.customer"
            ),
        ),
    ]
