from django.db import models
from .common import slugify


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    icon = models.ImageField('Image',upload_to='icons/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'
        ordering = ['title']


class Logo(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField('Image',upload_to='images/', null=False, blank=False)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Logo, self).save(*args, **kwargs)
        self.slug = slugify(self.title)
        super(Logo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Loqo'
        verbose_name_plural = 'Loqolar'
        ordering = ['title']


class HeaderText(models.Model):
    content = models.TextField('Content')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Bashliq teksti'
        verbose_name_plural = 'Bashliq tekstleri'
        ordering = ['content']
