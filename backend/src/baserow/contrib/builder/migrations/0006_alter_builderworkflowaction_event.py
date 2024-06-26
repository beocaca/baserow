# Generated by Django 4.1.13 on 2024-03-19 12:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("builder", "0005_textelement_format"),
    ]

    operations = [
        migrations.AlterField(
            model_name="builderworkflowaction",
            name="event",
            field=models.CharField(
                choices=[
                    ("click", "Click"),
                    ("submit", "Submit"),
                    ("after_login", "After Login"),
                ],
                help_text="The event that triggers the execution",
                max_length=30,
            ),
        ),
    ]
