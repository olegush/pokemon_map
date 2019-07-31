from django.contrib import admin
from .models import Pokemon, PokemonEntity, PokemonElementType


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'title_en', 'title_jp', 'get_element_types_str')

class PokemonElementTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_elements_strong_against')

admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonEntity)
admin.site.register(PokemonElementType, PokemonElementTypeAdmin)
