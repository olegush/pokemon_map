from django.db import models


class PokemonElementType(models.Model):
    title = models.CharField('Стихия', max_length=200, default='')
    image = models.ImageField('Картинка', blank=True)
    strong_against = models.ManyToManyField('self', verbose_name='Против кого силен', blank=True)

    def __str__(self):
        return f'{self.title}'

    def get_elements_strong_against(self):
        return ', '.join(elements.title for elements in self.strong_against.all())

    get_elements_strong_against.short_description = 'Силен против'


class Pokemon(models.Model):
    title_ru = models.CharField('Название', max_length=200, default='')
    title_en = models.CharField('Название англ.', max_length=200, blank=True, default='')
    title_jp = models.CharField('Название яп.', max_length=200, blank=True, default='')
    image = models.ImageField('Картинка', null=True, blank=True)
    description = models.TextField('Описание', blank=True, default='')
    next_evolution = models.ForeignKey('self', verbose_name='В кого эволюционирует', blank=True, null=True, related_name='nextevolution', on_delete=models.SET_NULL)
    previous_evolution = models.ForeignKey('self', verbose_name='Из кого эволюционировал', blank=True, null=True, related_name='previousevolution', on_delete=models.SET_NULL)
    element_type = models.ManyToManyField(PokemonElementType)

    def __str__(self):
        return f'{self.title_ru}'

    def get_element_types_str(self):
        return ', '.join(type.title for type in self.element_type.all())

    get_element_types_str.short_description = 'Стихия'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.CASCADE)
    lat = models.FloatField('Широта', null=True, blank=True)
    long = models.FloatField('Долгота', null=True, blank=True)
    appeared_at = models.DateTimeField('Появляется', null=True, blank=True)
    disappeared_at = models.DateTimeField('Исчезает', null=True, blank=True)
    level = models.IntegerField('Уровень', null=True, blank=True)
    health = models.IntegerField('Здоровье', null=True, blank=True)
    strength = models.IntegerField('Атака', null=True, blank=True)
    defence = models.IntegerField('Защита', null=True, blank=True)
    stamina = models.IntegerField('Выносливость', null=True, blank=True)

    def __str__(self):
        return f'{self.pokemon}, уровень {self.level}'
