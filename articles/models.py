from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    tags = models.ManyToManyField('Tag', through='ArticleToTag', through_fields=('article', 'tag'),
                                  verbose_name='разделы')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название Раздела')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['-name']

    def __str__(self):
        return self.name


class ArticleToTag(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='Статья')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='раздел')
    is_main = models.BooleanField(default=False, verbose_name='основной')

    class Meta:
        ordering = ['-is_main', '-tag']
