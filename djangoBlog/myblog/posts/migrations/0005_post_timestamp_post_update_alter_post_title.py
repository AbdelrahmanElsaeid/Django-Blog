# Generated by Django 4.1.5 on 2023-02-06 18:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_post_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="timestamp",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post", name="update", field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(
                error_messages={
                    "blank": "This field is not full please try again",
                    "unique": "This title is not unique please try again ",
                },
                help_text="Must be unique",
                max_length=100,
            ),
        ),
    ]
