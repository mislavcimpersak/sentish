# Generated by Django 2.1.4 on 2018-12-17 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("feeds", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="feed",
            name="last_fetch_ts",
            field=models.DateTimeField(blank=True, null=True),
        )
    ]
