# Generated by Django 4.2 on 2023-05-28 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cadastro_usuario',
            fields=[
                ('id_usuario', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=50, null=True)),
                ('cpf', models.CharField(max_length=11)),
                ('endereco', models.CharField(max_length=150)),
            ],
        ),
    ]
