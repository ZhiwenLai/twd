from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
# This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
# The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username
class salesinfo(models.Model):
    image = models.ImageField(upload_to='sales_images', blank=True,null=True)
    breedname = models.ForeignKey(to='Dog',related_name='name',max_length=128, blank=True,null=True,on_delete='CASCADE',)
    description = models.TextField(verbose_name='describe', blank=True,null=True)
    color = models.CharField(max_length=20, blank=True,null=True)
    gender= models.CharField(max_length=20, blank=True,null=True)
    price = models.IntegerField( blank=True,null=True)
    contactnumber = models.IntegerField( blank=True,null=True)

class Dog(models.Model):
    breedname = models.CharField(max_length=128 ,blank=True,null=True)
    image = models.ImageField(upload_to='dog_images', blank=True,null=True)
    description = models.TextField(verbose_name='describe' ,blank=True,null=True)
    salesinfo = models.ForeignKey(to='salesinfo',on_delete='CASCADE',verbose_name='sales',blank=True,null=True)
    views = models.IntegerField(default=0)
    status_choices = (
        (1, 'samllDog'),
        (2, 'bigDog'),
        (3, 'mediumDog'),
    )
    status = models.SmallIntegerField(verbose_name='size', choices=status_choices, default=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collect_count = None

    def __str__(self):
        return self.breedname

class comment(models.Model):
    username = models.CharField(max_length=128,verbose_name='username',default='noone')
    content = models.TextField(verbose_name='content',null=True)
    date = models.DateTimeField(verbose_name='time',auto_now_add=True)

    class Meta:
        verbose_name = 'comments'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:5]

class collection(models.Model):
    clt_who = models.CharField(max_length=128, blank=True, null=True)
    clt_dogid = models.CharField(max_length=128, blank=True, null=True)
    clt_breedname = models.CharField(max_length=128, blank=True, null=True)
    clt_image = models.ImageField(upload_to='dog_images', blank=True, null=True)
    clt_description = models.TextField(verbose_name='describe', blank=True, null=True)

