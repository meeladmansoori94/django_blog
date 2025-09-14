from django.views.generic import ListView, DetailView, CreateView  # Add CreateView
from django.contrib.auth.mixins import LoginRequiredMixin  # Import the mixin
from django.urls import reverse_lazy  # Used to safely find a URL
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    # Django automatically passes the data to the template as 'object_list'
    # We rename it 'posts' to make our template more readable.
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    # This tells DetailView to look up the post using the 'slug' field
    # in the URL, rather than the default primary key (pk/id).
    slug_field = "slug"
    # This matches the key we will use in the URL (step 2)
    slug_url_kwarg = "slug"


# LoginRequiredMixin MUST come BEFORE CreateView.
# This acts as a middleware: if the user is not logged in, it redirects them to the LOGIN_URL.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    # We only need the user to fill out these fields
    fields = ["title", "slug", "body"]
    # This tells Django where to redirect after a successful form submission
    # We use reverse_lazy because the URLs are not loaded when this file is imported.
    success_url = reverse_lazy("blog:list")

    # We must override this method to automatically set the post author to the logged-in user.
    def form_valid(self, form):
        # Automatically set the author to the current logged-in user.
        form.instance.author = self.request.user
        return super().form_valid(form)
