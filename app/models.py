from django.db import models
from colorfield.fields import ColorField
from ckeditor.fields import RichTextField

# Create your models here.


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
    image = models.ImageField(upload_to='project/')
    cover = models.ImageField(upload_to='project/')
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