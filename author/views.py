from django.shortcuts import render, redirect
from .models import *
import string
import random
from .forms import *
# Create your views here.


def authors(request):
    authors_list = Author.objects.all()
    context = {
        'authors': authors_list
    }
    return render(request, "pages/authors.html", context)


def add_author(request):
    letters = string.ascii_lowercase
    for_author = []
    for i in range(3):
        word = ''.join(random.choice(letters)for i in range(4, 10))
        for_author.append(word)
    Author.create(
        name=for_author[0], surname=for_author[1], patronymic=for_author[2])
    # if request.method == "POST":
    #     form = AddAuthor(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("all_books")
    # else:
    #     form = AddAuthor()
#    return render(request, 'pages/add_author.html')
    return redirect('authors:authors')


def delete_authors(request):
    all_authors = Author.objects.all()
    all_authors.delete()
    return redirect('authors:authors')


def edit_author(request, author_id):
    if request.method == "GET":
        if id == 0:
            form = EditAuthor()
        else:
            author = Author.get_by_id(author_id)
            form = EditAuthor(instance=author)
        return render(request, "pages/edit_author.html", context={"form": form, "id": author_id})
    else:
        author = Author.get_by_id(author_id)
        form = EditAuthor(request.POST, instance=author)
    if form.is_valid():
        form.save()
    return redirect("authors:authors")
