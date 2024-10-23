# Generated by Django 4.2.2 on 2024-10-23 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_talk_options'),
        ('registration', '0003_auto_20240926_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='name_speaker',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome do Palestrante'),
        ),
        migrations.AddField(
            model_name='registration',
            name='start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Horário de Início'),
        ),
        migrations.AddField(
            model_name='registration',
            name='talk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='registrations_as_talks', to='core.talk', verbose_name='Nome da Palestra'),
        ),
    ]