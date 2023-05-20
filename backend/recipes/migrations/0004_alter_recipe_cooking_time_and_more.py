# Generated by Django 4.2.1 on 2023-05-20 13:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0003_alter_recipeingredient_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="cooking_time",
            field=models.PositiveSmallIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=1,
                        message="Время приготовления не может быть менее одной минуты.",
                    ),
                    django.core.validators.MaxValueValidator(
                        limit_value=300, message="Очень долго ждать..."
                    ),
                ],
                verbose_name="Время приготовления",
            ),
        ),
        migrations.AlterField(
            model_name="recipeingredient",
            name="amount",
            field=models.PositiveSmallIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=0.01, message="Количество должно быть больше нуля!"
                    ),
                    django.core.validators.MaxValueValidator(
                        limit_value=32, message="Слишком много!"
                    ),
                ],
                verbose_name="Количество",
            ),
        ),
    ]
