from django.views.generic import ListView, DetailView
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
