# Generated by Django 3.2.16 on 2022-11-16 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('mensaje', models.CharField(max_length=1000)),
            ],
        ),
    ]
