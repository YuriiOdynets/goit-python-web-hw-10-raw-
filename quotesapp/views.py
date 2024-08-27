from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .forms import AuthorForm, QuoteForm
from .models import Author, Quote

# Create your views here.
def main(request):
    quotes = Quote.objects.all().order_by('author')
    elems_per_page = 5
    paginator = Paginator(quotes, elems_per_page)
    page = request.GET.get('page')

    try:
        quotes = paginator.page(page)
    except PageNotAnInteger:
        quotes = paginator.page(1)
    except EmptyPage:
        quotes = paginator.page(paginator.num_pages)

    context = {
        'quotes': quotes
    }

    return render(request, 'quotesapp/index.html', context=context)

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect(to='quotesapp:index')
        else:
            return render(request, 'quotesapp/add_author.html', {'form': form})
        
    return render(request, 'quotesapp/add_author.html', {'form':AuthorForm()})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            return redirect(to='quotesapp:index')
        else:
            return render(request, 'quotesapp/add_quote.html', {'form':form})
    return render(request, 'quotesapp/add_quote.html', {'form': QuoteForm()})


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'quotesapp/detail.html', {'author': author})

@login_required
def delete_quote(request, quote_id):
    Quote.objects.get(pk=quote_id).delete()
    return redirect(to='quotesapp:index')

@login_required
def delete_author(request, author_id):
    Author.objects.get(pk=author_id).delete()
    return redirect(to='quotesapp:index')