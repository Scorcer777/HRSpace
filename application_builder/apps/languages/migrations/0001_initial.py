# Generated by Django 4.2.1 on 2024-03-24 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageProficiency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proficiency_level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Fluent', 'Fluent')], max_length=100)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.language')),
            ],
        ),
    ]
