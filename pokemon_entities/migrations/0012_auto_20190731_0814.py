# Generated by Django 2.2.3 on 2019-07-31 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_auto_20190731_0656'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonElementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200, verbose_name='Стихия')),
            ],
        ),
        migrations.AddField(
            model_name='pokemon',
            name='element_type',
            field=models.ManyToManyField(to='pokemon_entities.PokemonElementType'),
        ),
    ]
