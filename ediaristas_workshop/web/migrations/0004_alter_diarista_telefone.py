# Generated by Django 4.0a1 on 2021-10-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_diarista_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diarista',
            name='telefone',
            field=models.CharField(default=False, max_length=11),
        ),
    ]