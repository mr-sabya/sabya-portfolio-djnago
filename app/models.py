from django.db import models
from colorfield.fields import ColorField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user/')
    short_description = models.TextField(max_length=255)
    details = RichTextField()

    def __str__(self):
        return self.user.first_name



class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title
    

class Type(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    company = models.CharField(max_length=150, null=True, blank=True)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='client/')
    details = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.name
    


class Language(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='language/', null=True, blank=True)

    def __str__(self):
        return self.name
    


class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    link = models.CharField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project/', help_text="Image size must be 768*576 px")
    cover = models.ImageField(upload_to='project/', help_text="Image size must be 1900*835 px")
    client = models.ForeignKey(Client, on_delete=models.Case)
    date = models.DateField()
    details = RichTextField()
    language = models.ManyToManyField(Language)

    def __str__(self):
        return self.title
    

class Project_Feature(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    feature = models.CharField(max_length=255)


class Project_image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='project/', null=True, blank=True)




class Service(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='service/')
    details = models.TextField( max_length=255)

    def __str__(self):
        return self.title
    


class Skill(models.Model):
    title = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='skill/')
    percentage = models.IntegerField()

    def __str__(self):
        return self.title
    


class Education(models.Model):
    degree = models.CharField(max_length=100)
    college = models.CharField(max_length=150)
    date = models.CharField(max_length=50)
    details = models.TextField(max_length=200)

    def __str__(self):
        return self.degree
    

FREELANCE_STATUS = (
    ('Available','Available'),
    ('Unavailable','Unavailable'),

)

class Info(models.Model):
    name = models.CharField(max_length=255)
    birth_day = models.DateField()
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    skype = models.CharField(max_length=100)
    freelance = models.CharField(max_length=15, choices=FREELANCE_STATUS, default="Available")

    def __str__(self):
        return self.name
    


class Brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='brands/')

    def __str__(self):
        return self.name



class Feedback(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    feedback = models.TextField(max_length=255)

    def __str__(self):
        return self.client.name
    


class BlogCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title
    


class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title
    

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project/', help_text="Image size must be 800*600 px")
    cover = models.ImageField(upload_to='project/', help_text="Image size must be 1500*840 px")
    blog = RichTextField()
    tags = models.ManyToManyField(Tag)
    meta_description = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.title
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.blog.title
    
    class Meta:
        ordering = ('created_at', )
    

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    reply = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)




#pricing
class Pricing(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    price = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Pricing_Options(models.Model):
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE)
    option = models.CharField(max_length=255)




STATUS_CHOICES = (
    ('pending','Pending'),
    ('received', 'Received'),
    ('running','Running'),
    ('completed','Completed'),
    ('canceled','Canceled'),
)

class Order(models.Model):
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    details = models.TextField()
    budget = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")






