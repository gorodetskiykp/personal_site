from django.db import models


class Category(models.Model):
    title = models.CharField('Категория', max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
