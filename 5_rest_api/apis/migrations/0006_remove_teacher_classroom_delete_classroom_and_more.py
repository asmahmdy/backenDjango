# Generated by Django 5.0.6 on 2024-06-02 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='classroom',
        ),
        migrations.DeleteModel(
            name='Classroom',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]