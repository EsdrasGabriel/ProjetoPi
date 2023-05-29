# Generated by Django 4.2 on 2023-05-29 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_cadastro_usuario_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro_usuario',
            name='cpf',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='cadastro_usuario',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
