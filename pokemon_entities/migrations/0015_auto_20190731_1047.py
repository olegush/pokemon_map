# Generated by Django 2.2.3 on 2019-07-31 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0014_pokemonelementtype_strong_against'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonelementtype',
            name='strong_against',
            field=models.ManyToManyField(blank=True, related_name='_pokemonelementtype_strong_against_+', to='pokemon_entities.PokemonElementType', verbose_name='Против кого силен'),
        ),
    ]
