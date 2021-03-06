# Generated by Django 2.1.4 on 2018-12-18 17:26

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("content", "0004_auto_20181218_0012")]

    operations = [
        migrations.AddField(
            model_name="article",
            name="sentiment_calculated_ts",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="sentiment_details",
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name="article",
            name="sentiment_score",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="article",
            name="status",
            field=models.CharField(
                choices=[
                    ("created", "Created"),
                    ("content_fetched", "Content Fetched"),
                    ("response_error", "Response Error"),
                    ("sentiment_set", "Sentiment Set"),
                    ("sentiment_error", "Sentiment Error"),
                ],
                default="created",
                max_length=30,
            ),
        ),
    ]
