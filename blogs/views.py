from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blogs.models import BlogPost


def blog_main(request):
    return render(request, 'blogs/blogpost_main_page.html')


class BlogPostListView(ListView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.publication is True:
            self.object.save()
            return self.object


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ("title", "description", "preview", "publication")
    success_url = reverse_lazy('blogs:blogpost_list')

    def form_valid(self, form):
        if form.is_valid():
            model = form.save()
            model.slug = slugify(BlogPost.title)
            model.save()
        return super().form_valid(form)



class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ("title", "description", "preview", "publication")
    success_url = reverse_lazy('blogs:blogpost_list')

    def get_success_url(self):
        return reverse('blogs:post', args=[self.kwargs.get('pk')])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogs:blogpost_list')
