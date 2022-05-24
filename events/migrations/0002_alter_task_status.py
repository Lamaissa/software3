# Generated by Django 3.2.12 on 2022-05-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Back Burner', 'Back Burner'), ('On Deck', 'On Deck'), ('In Process', 'In Process'), ('Complete', 'Complete')], default='', max_length=20),
        ),
    ]
