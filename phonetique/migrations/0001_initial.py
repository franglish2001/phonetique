# Generated by Django 5.1.4 on 2024-12-31 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextTransformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_text', models.TextField()),
                ('transformed_text', models.TextField(blank=True)),
                ('fonction', models.TextField()),
            ],
        ),
    ]