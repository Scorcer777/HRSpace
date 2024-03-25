# Generated by Django 4.2.1 on 2024-03-24 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('industries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='industries.industry')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professions.profession')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professions.skill')),
            ],
            options={
                'unique_together': {('profession', 'skill')},
            },
        ),
    ]
