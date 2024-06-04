# Generated by Django 5.0.6 on 2024-06-02 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_class', models.CharField(max_length=100, null=True)),
                ('classroom_no', models.CharField(max_length=100, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.school')),
            ],
        ),
    ]
