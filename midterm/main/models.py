from django.db import models
from utils.constants import JOURNAL_TYPES, TYPE_BULLET

# Create your models here.
class BookJournalBase(models.Model):
    # i.name
    # ii.price
    # iii.description
    # iv.created_at

    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Book(BookJournalBase):

    # i.num_pages
    # ii.genre

    num_pages = models.PositiveIntegerField(verbose_name='Количество страниц')
    genre = models.CharField(max_length=255, verbose_name='Жанр')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Journal(BookJournalBase):
    # i.type[Bullet, Food, Travel, Sport]
    # ii.publisher

    type = models.SmallIntegerField(choices=JOURNAL_TYPES, default=TYPE_BULLET, verbose_name='Тип')
    publisher = models.CharField(max_length=255, verbose_name='Издатель')

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'

