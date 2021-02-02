from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book


class BookList(LoginRequiredMixin, ListView):
    model = Book


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'pages', 'date']
    success_url = reverse_lazy('books_cbv:book_list')


class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'pages', 'date']
    success_url = reverse_lazy('books_cbv:book_list')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books_cbv:book_list')