from django.db import models

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
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    


class Language(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='language/', null=True, blank=True)
    


class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project/')
    cover = models.ImageField(upload_to='project/')
    client = models.ForeignKey(Client, on_delete=models.Case)
    date = models.DateField()
    details = models.TextField()
    language = models.ManyToManyField(Language)

    def __str__(self):
        return self.title
    

class Project_Feature(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    feature = models.CharField(max_length=255)