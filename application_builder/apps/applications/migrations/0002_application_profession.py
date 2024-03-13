# Generated by Django 5.0.3 on 2024-03-13 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
        ('professions', '0002_alter_profession_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='profession',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='professions.profession'),
            preserve_default=False,
        ),
    ]
