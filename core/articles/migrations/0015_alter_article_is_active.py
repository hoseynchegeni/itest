# Generated by Django 4.2.6 on 2023-11-08 15:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0014_remove_article_is_checked"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
