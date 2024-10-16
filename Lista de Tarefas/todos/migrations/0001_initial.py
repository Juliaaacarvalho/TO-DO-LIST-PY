# Generated by Django 5.1.1 on 2024-09-20 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100, verbose_name='Nome da Tarefa')),
                ('creation', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('delivery', models.DateField(verbose_name='Data de entrega')),
                ('finalization', models.DateField(null=True)),
            ],
        ),
    ]
