# Generated by Django 4.0a1 on 2021-10-13 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_diarista_cep'),
    ]

    operations = [
        migrations.AddField(
            model_name='diarista',
            name='telefone',
            field=models.CharField(default=True, max_length=11),
        ),
    ]
