# Generated by Django 4.2 on 2023-05-04 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.CharField(max_length=15)),
                ("sal", models.IntegerField()),
                ("city", models.CharField(max_length=60)),
                ("state", models.CharField(max_length=60)),
            ],
        ),
    ]
