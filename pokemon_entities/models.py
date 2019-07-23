from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField('Название', max_length=200, null=True)
    title_en = models.CharField('Название англ.', max_length=200, null=True)
    title_jp = models.CharField('Название яп.', max_length=200, null=True)
    image = models.ImageField('Картинка', null=True, blank=True)
    description = models.TextField('Описание', null=True, blank=True)
    next_evolution = models.ForeignKey('self', verbose_name='В кого эволюционирует', blank=True, null=True, related_name='nextevolution', on_delete=models.CASCADE)
    previous_evolution = models.ForeignKey('self', verbose_name='Из кого эволюционировал', blank=True, null=True, related_name='previousevolution', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title_ru}'

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.CASCADE)
    lat = models.FloatField('Широта')
    long = models.FloatField('Долгота')
    appeared_at = models.DateTimeField('Появляется', null=True, default=None, blank=True)
    disappeared_at = models.DateTimeField('Исчезает', null=True, default=None, blank=True)
    level = models.IntegerField('Уровень', null=True, blank=True)
    health = models.IntegerField('Здоровье', null=True, blank=True)
    strength = models.IntegerField('Атака', null=True, blank=True)
    defence = models.IntegerField('Защита', null=True, blank=True)
    stamina = models.IntegerField('Выносливость', null=True, blank=True)

    def __str__(self):
        return f'{self.pokemon}, уровень {self.level}'
