# Generated by Django 4.2.2 on 2024-02-17 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_speaker_options_alter_speaker_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('E', 'Email'), ('P', 'Telefone')], max_length=1)),
                ('value', models.CharField(max_length=255)),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.speaker')),
            ],
        ),
    ]