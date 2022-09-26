from django.db import models


class Link(models.Model):
    link = models.URLField('Ссылка', unique=True)
    categories = models.ManyToManyField(
        'tech.Category',
        verbose_name='Категории',
        blank=True,
        related_name='links',
    )
    description = models.CharField('Описание', max_length=200)

    def __str__(self):
        return '{}. {}'.format(self.categories_list, self.description)

    class Meta:
        ordering = ('description', )
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    @property
    def categories_list(self):
        return ', '.join([category.title for category in self.categories.all()])
