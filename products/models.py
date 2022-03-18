from django.db import models
from .common import slugify
from accounts.models import User
import random
from ckeditor_uploader.fields import RichTextUploadingField


class Order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=3000)
    zip_code = models.CharField(max_length=3000)
    email = models.EmailField(('email adress'), null=True, blank=True)
    number = models.CharField(('Number'),max_length=100, null=True, blank=True)
    order_notes = models.TextField('Text', null=True, blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, db_index=True, related_name='orders', null=True, blank=True)
    status = models.CharField(max_length=200)
    # seller = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='orders', null=True, blank=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='orders', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} in sifarishi'

    class Meta:
        verbose_name = 'Sifarish'
        verbose_name_plural = 'Sifarishler'
        # ordering = ['title']


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
    brand = models.CharField(max_length=100, null=True, blank=True)
    main_image = models.ImageField('Image',upload_to='images/', null=True, blank=True)
    video = models.CharField(max_length=3000)
    rating = models.PositiveSmallIntegerField('rating', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    sub_sub_category = models.ForeignKey(SubSubCategory, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='products', null=True, blank=True)
    tag = models.ManyToManyField('Tag', db_index=True, related_name='products', null=True, blank=True)
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


class DiscountProduct(models.Model):
    discount_price = models.DecimalField('Price',max_digits=6, decimal_places=2)
    time_range = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, related_name='discount_products') 
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Endirimli mehsul'
        verbose_name_plural = 'Endirimli mehsullar'

    def __str__(self):
        return self.product.title


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


class Tag(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Taglar'

    def __str__(self):
        return self.title


class FAQCategory(models.Model):
    title = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Tez Tez verilen sual Bolmesi'
        verbose_name_plural = 'Tez Tez verilen suallar Bolmesi'

    def __str__(self):
        return self.title



class FAQ(models.Model):
    question = models.TextField("Question")
    answer = models.TextField("Answer")
    category = models.ForeignKey(FAQCategory, on_delete=models.CASCADE, db_index=True, related_name='faqs', null=True, blank=True)

    class Meta:
        verbose_name = 'Tez Tez verilen sual'
        verbose_name_plural = 'Tez Tez verilen suallar'

    def __str__(self):
        return self.question


class AboutUs(models.Model):
    content = RichTextUploadingField()
    service_title = models.CharField(max_length=1000)
    service_image = models.ImageField('Image',upload_to='images/', null=True, blank=True)
    services = models.ManyToManyField('AboutUsService', db_index=True, related_name='aboutus', null=True, blank=True)
    corousel = models.ManyToManyField('AboutUsCarousel', db_index=True, related_name='aboutus', null=True, blank=True)
    banner_title = models.CharField(max_length=1000)
    banner_image = models.ImageField('Image',upload_to='images/', null=True, blank=True)
    banner_text = models.TextField("Banner Text")
    banner_button_text = models.CharField(max_length=1000)
    banner_button_link = models.CharField(max_length=10000)

    class Meta:
        verbose_name = 'Haqqimizda'
        verbose_name_plural = 'Haqqimizda'


class AboutUsService(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField("Description")

    class Meta:
        verbose_name = 'Haqqimizda Servisi'
        verbose_name_plural = 'Haqqimizda Servisleri'


class AboutUsCarousel(models.Model):
    title = models.CharField(max_length=1000)
    amount = models.IntegerField()
    description = models.TextField("Description")

    class Meta:
        verbose_name = 'Haqqimizda Servisi'
        verbose_name_plural = 'Haqqimizda Servisleri'


class UserMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(('email adress'), unique=False, null=True, blank=True)
    message = models.TextField("Message")

    class Meta:
        verbose_name = 'Istifadeci mesaji'
        verbose_name_plural = 'Istifadeci mesajlari'

    def __str__(self):
        return self.name


class Rating(models.Model):
    RATING_CHOICES = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )

    author = models.ForeignKey(User,on_delete=models.CASCADE, db_index=True, related_name='ratings')
    rating = models.PositiveSmallIntegerField('rating',choices=RATING_CHOICES)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, db_index=True, related_name='ratings')

    def __str__(self):
        return f'{self.author} > {self.product} rating'


    def save(self, *args, **kwargs):
        print(self.product)
        rat_numbers = list(map(lambda e: e.rating, self.product.ratings.all()))
        if rat_numbers:
            print(sum(rat_numbers)//len(rat_numbers))
            self.product.rating = sum(rat_numbers)//len(rat_numbers)
            self.product.save()
        super(Rating, self).save(*args, **kwargs)
    
    class Meta:
        unique_together = ('author','product')


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(('email adress'), unique=False, null=True, blank=True)
    review = models.TextField("Review")
    product = models.ForeignKey("Product", on_delete=models.CASCADE, db_index=True, related_name='comments')

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_index=True, related_name='wishlist')
    product = models.ManyToManyField(Product, verbose_name=("Product"), db_index=True, related_name='wishlist', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    def __str__(self):
        return f"{self.user.number}'s Wishlist"


class ProductVersion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, related_name='product_version', null=False, blank=True)
    final_price = models.DecimalField('Price',max_digits=6, decimal_places=2, blank=True)
    quantity = models.IntegerField('Quantity',blank=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Product Version'
        verbose_name_plural = 'Product Versions'

    def __str__(self):
        return f"{self.product.title}"

    def save(self, *args, **kwargs):
        quantity = int(self.quantity)
        price = int(self.product.price)
        self.final_price =  quantity*price
        super(ProductVersion, self).save(*args, **kwargs)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_index=True, related_name='user_cart')
    product_version = models.ManyToManyField(ProductVersion, verbose_name=("Product Version"), db_index=True, related_name='cart_product', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
    
    def __str__(self):
        return f"{self.user.number}'s Cart"
        

class CategoryBanner(models.Model):
    image = models.ImageField('Image',upload_to='images/', null=True, blank=True)
    button_text = models.CharField(max_length=100)
    button_link = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Kateqoriya Reklam Banneri'
        verbose_name_plural = 'Kateqoriya Reklam Bannerleri'
    
    def __str__(self):
        return self.button_text


class Number(models.Model):
    number = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Bize zeng edin nomresi'
        verbose_name_plural = 'Bize zeng edin nomreleri'
    
    def __str__(self):
        return self.number


class Subscriber(models.Model):
    email = models.EmailField(('email adress'), unique=False, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
    
    def __str__(self):
        return self.email