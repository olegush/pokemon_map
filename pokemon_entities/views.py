# TODO: image urls

import folium
import json

from django.conf import settings
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_list_or_404, get_object_or_404
from pokemon_entities.models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"
HOST = 'http://127.0.0.1:8000'

def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = get_list_or_404(Pokemon)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons_on_page = []
    for pokemon in pokemons:
        img_url = pokemon.image.url if pokemon.image else ''
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': img_url,
            'title_ru': pokemon.title_ru,
        })
        pokemon_entities = get_list_or_404(PokemonEntity, pokemon=pokemon.id)
        for pokemon_entity in pokemon_entities:
            add_pokemon(
                folium_map, pokemon_entity.lat, pokemon_entity.long,
                pokemon.title_ru, f'{HOST}{pokemon.image.url}')
    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })

from django.forms.models import model_to_dict
def show_pokemon(request, pokemon_id):
    pokemon = model_to_dict(get_object_or_404(Pokemon, id=pokemon_id))
    pokemon['img_url'] = f"{HOST}{pokemon['image'].url}"
    if pokemon['next_evolution']:
        pokemon_next_evolution = Pokemon.objects.get(id=pokemon['next_evolution'])
        pokemon['next_evolution'] = {
                    'pokemon_id': pokemon_next_evolution.id,
                    'title_ru': pokemon_next_evolution.title_ru,
                    'img_url': f'{HOST}{pokemon_next_evolution.image.url}'}
    if pokemon['previous_evolution']:
        pokemon_previous_evolution = Pokemon.objects.get(id=pokemon['previous_evolution'])
        pokemon['previous_evolution'] = {
                    'pokemon_id': pokemon_previous_evolution.id,
                    'title_ru': pokemon_previous_evolution.title_ru,
                    'img_url': f'{HOST}{pokemon_previous_evolution.image.url}'}
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = get_list_or_404(PokemonEntity, pokemon=pokemon_id)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.long,
            pokemon['title_ru'], pokemon['img_url'])
    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon})
