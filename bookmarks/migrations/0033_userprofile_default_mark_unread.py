# Generated by Django 5.0.3 on 2024-04-17 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookmarks", "0032_html_snapshots_hint_toast"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="default_mark_unread",
            field=models.BooleanField(default=False),
        ),
    ]
