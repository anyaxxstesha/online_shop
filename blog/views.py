from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from unidecode import unidecode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return self.model.objects.filter(is_published=True).order_by("-created_at")


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_amount += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = Post
    fields = ("title", "content", "preview_image")
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(unidecode(new_post.title))
            new_post.save()

        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ("title", "content", "preview_image")

    def get_success_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
