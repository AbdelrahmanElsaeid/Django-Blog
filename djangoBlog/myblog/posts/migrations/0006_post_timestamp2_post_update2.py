# Generated by Django 4.1.5 on 2023-02-06 18:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_post_timestamp_post_update_alter_post_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="timestamp2",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="update2",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
