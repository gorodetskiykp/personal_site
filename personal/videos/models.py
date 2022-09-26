from django.db import models


class Category(models.Model):
    title = models.CharField('Категория', max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Link(models.Model):
    link = models.URLField('Ссылка', unique=True)
    description = models.CharField('Описание', max_length=200)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ('description', )
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'


class Video(models.Model):
    link = models.URLField('Ссылка', unique=True)
    categories = models.ManyToManyField(
        Category,
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
    links = models.ManyToManyField(
        Link,
        verbose_name='Дополнительные ссылки',
        blank=True,
        related_name='videos',
    )

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ('title', )
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
