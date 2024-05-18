from django.db import models

class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="название",
        help_text="Введите название группы",
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="уникальный фрагмент URL-адреса",
        help_text="Введите уникальный фрагмент URL-адреса для группы",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание группы"
    )

    class Meta:
        verbose_name = ('група')
        verbose_name_plural = ('Группы')

    def __str__(self) -> str:
        return self.title
