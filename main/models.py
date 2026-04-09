from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField()

    @property
    def num(self):
        return self.book.count()

    def __str__(self):
        return self.name


class Category(models.Model):
    sort = models.CharField(max_length=255)

    @property
    def num(self):
        return self.book.count()

    def __str__(self):
        return self.sort
    

class Book(models.Model):
    sort = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='book')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name='book')
    price = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title