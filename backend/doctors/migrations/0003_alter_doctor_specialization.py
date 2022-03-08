# Generated by Django 4.0.3 on 2022-03-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_alter_doctor_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(choices=[('dermatologist', 'dermatologist'), ('psychiatrist', 'psychiatrist'), ('neurologist', 'neurologist'), ('physician', 'physician')], max_length=20),
        ),
    ]
