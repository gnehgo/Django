# Generated by Django 4.1.6 on 2023-02-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nba', '0004_alter_gamestat_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamestat',
            name='score',
            field=models.CharField(db_column='score', max_length=50),
        ),
    ]
