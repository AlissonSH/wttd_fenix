# Generated by Django 4.2.2 on 2024-02-26 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_course_abc_to_mti'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CourseOld',
        ),
    ]
