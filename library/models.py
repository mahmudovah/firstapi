from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

class Author(models.Model):
    name = models.CharField(max_length=255)
    birth = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
    

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='books')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    name = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name