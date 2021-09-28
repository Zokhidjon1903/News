from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Sarlavhasi")
    content = models.TextField(blank=True, verbose_name='Yangilik matni')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    updated_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name="Rasm")
    is_published = models.BooleanField(default=True, verbose_name="Chop qilinganligi")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Yangilik turi")
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

    def myFunc(self):
        return "News modelidan salomlar"

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Yangilik turi')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Yangilik turi'
        verbose_name_plural = 'Yangilik turlari'
