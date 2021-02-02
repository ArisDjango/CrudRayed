from django.db import models
from django.urls import reverse
from django.utils.timezone import now

class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()
    date = models.DateField(now)
    note = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_cbv:book_edit', kwargs={'pk': self.pk})