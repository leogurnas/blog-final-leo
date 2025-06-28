from django.shortcuts import render, get_object_or_404
from .models import Page
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

def page_list(request):
    pages = Page.objects.all()
    return render(request, 'pages/page_list.html', {'pages': pages})

def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'pages/page_detail.html', {'page': page})

def about(request):
    return render(request, 'pages/about.html')

def home_view(request):
    return render(request, 'home.html')

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image', 'date']
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('page_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image', 'date']
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('page_list')
