from django.db import models


class Video(models.Model):
    link = models.URLField('Ссылка', unique=True)
    categories = models.ManyToManyField(
        'tech.Category',
        verbose_name='Категории',
        blank=True,
        related_name='videos',
    )
    title = models.CharField('Название', max_length=200)
    description = models.CharField('Описание', max_length=200, null=True, blank=True)
    language = models.CharField('Язык', max_length=2, choices=[('ru', 'RU'), ('en', 'EN')], default='RU')
    difficult = models.CharField(
        'Сложность',
        max_length=20,
        choices=[
            ('1', 'начальный уровень'),
            ('2', 'требуется подготовка'),
            ('3', 'для профи')
        ],
        default='1',
    )
    author_github_link = models.URLField('Ссылка на проект автора в GitHub', null=True, blank=True, unique=True)
    my_github_link = models.URLField('Ссылка на мой проект в GitHub', null=True, blank=True, unique=True)

    def __str__(self):
        return '{}. {}'.format(self.categories_list, self.title)

    class Meta:
        ordering = ('title', )
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    @property
    def categories_list(self):
        return ', '.join([category.title for category in self.categories.all()])
