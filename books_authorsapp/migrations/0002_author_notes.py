# Generated by Django 2.2.4 on 2020-06-15 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authorsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]