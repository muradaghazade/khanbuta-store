from django.db import models
from .common import slugify
from accounts.models import User
import random


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


class FilterValue(models.Model):
    value = models.CharField(max_length=200)
    the_filter = models.ForeignKey(Filter, on_delete=models.CASCADE, related_name='values', blank=False, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='filter_values', blank=False, null=True)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Filter Value'
        verbose_name_plural = 'Filter Values'

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
        verbose_name = 'Xidmet'
        verbose_name_plural = 'Xidmetler'


class Partner(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField('Image',upload_to='images/', null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Partnyor'
        verbose_name_plural = 'Partnyorlar'


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField('Description')
    code = models.CharField(max_length=50, blank=True)
    price = models.DecimalField('Price',max_digits=6, decimal_places=2)
    short_desc1 = models.CharField(max_length=1000)
    short_desc2 = models.CharField(max_length=1000)
    short_desc3 = models.CharField(max_length=1000)
    main_image = models.ImageField('Image',upload_to='images/', null=False, blank=False)
    sub_sub_category = models.ForeignKey(SubSubCategory, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='products', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Mehsul'
        verbose_name_plural = 'Mehsullar'

    def save(self, *args, **kwargs):
        num_list = [i for i in range(10)]
        code_items = []

        for i in range(6):
            num = random.choice(num_list)
            code_items.append(num)

        code = "".join(str(item) for item in code_items)
        self.code = f'{code}{self.id}'
        super(Product, self).save(*args, **kwargs)


class Image(models.Model):
    image = models.ImageField('Image',upload_to='images/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, related_name='images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Shekil'
        verbose_name_plural = 'Shekiller'

    def __str__(self):
        return self.product.title