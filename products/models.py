from django.db import models
from .common import slugify


class CategoryLine(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='categories', blank=True, null=True)

    def __str__(self):
        return self.category.title

    class Meta:
        verbose_name = 'Qara Lent Kategoriya'
        verbose_name_plural = 'Qara Lent Kategoriyalari'
        # ordering = ['title']


class DisplayedCategory(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='dis_categories', blank=True, null=True)

    def __str__(self):
        return self.category.title

    class Meta:
        verbose_name = 'Ana Sehife Kategoriya'
        verbose_name_plural = 'Ana Sehife Kategoriyalari'


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    icon = models.ImageField('Image',upload_to='icons/', null=False, blank=False)
    slug = models.SlugField(max_length=200, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'
        ordering = ['title']


class SubCategory(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories', blank=True, null=True)
    # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=200, editable=False, null=True)
    icon = models.ImageField('Icon',upload_to='icons/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Alt kateqoriya"
        verbose_name_plural = "Alt kateqoriyalar"
        ordering = ['title']

    def save(self, *args, **kwargs):
        super(SubCategory, self).save(*args, **kwargs)
        self.slug = slugify(self.title)
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class SubSubCategory(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='sub_sub_categories', blank=True, null=True)
    # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=200, editable=False, null=True)
    icon = models.ImageField('Icon',upload_to='icons/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Alt Alt kateqoriya"
        verbose_name_plural = "Alt Alt kateqoriyalar"
        ordering = ['title']

    def save(self, *args, **kwargs):
        super(SubSubCategory, self).save(*args, **kwargs)
        self.slug = slugify(self.title)
        super(SubSubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Filter(models.Model):
    title = models.CharField(max_length=200)
    sub_sub_category = models.ForeignKey(SubSubCategory, on_delete=models.CASCADE, related_name='filters', blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, editable=False, null=True)

    class Meta:
        verbose_name = "Filter"
        verbose_name_plural = "Filterler"
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Filter, self).save(*args, **kwargs)
        self.slug = slugify(self.title)
        super(Filter, self).save(*args, **kwargs)


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


class Slider(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField('Description')
    image = models.ImageField('Image',upload_to='images/', null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliderler'


class Benefit(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField('Description')
    icon = models.ImageField('Image',upload_to='icons/', null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Xidmetler'
        verbose_name_plural = 'Xidmetler'