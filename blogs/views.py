from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blogs.models import BlogPost


def blog_main(request):
    return render(request, 'blog_pages/blogpost_main_page.html')


class BlogPostListView(ListView):
    model = BlogPost


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ("title", "slug", "description", "preview", "publication")
    success_url = reverse_lazy('blog_pages:blogpost_list')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ("title", "slug", "description", "preview", "publication")
    success_url = reverse_lazy('blog_pages:blogpost_list')

    def get_success_url(self):
        return reverse('blog_pages:post', args=[self.kwargs.get('pk')])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog_pages:blogpost_list')
