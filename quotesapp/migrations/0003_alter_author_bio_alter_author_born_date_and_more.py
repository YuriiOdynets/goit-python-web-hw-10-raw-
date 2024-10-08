# Generated by Django 5.1 on 2024-08-25 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotesapp', '0002_remove_quote_created_by_author_user_quote_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='born_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotesapp.author'),
        ),
    ]
