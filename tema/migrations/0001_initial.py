# Generated by Django 2.2.5 on 2019-10-29 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor_aluguel', models.IntegerField()),
                ('cor_toalha', models.CharField(max_length=100)),
            ],
        ),
    ]
