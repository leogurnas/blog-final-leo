from django.shortcuts import render, get_object_or_404
from .models import Page

def page_list(request):
    pages = Page.objects.all()
    return render(request, 'pages/page_list.html', {'pages': pages})

def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'pages/page_detail.html', {'page': page})

def about(request):
    return render(request, 'pages/about.html')

