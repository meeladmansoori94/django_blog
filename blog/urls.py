from django.urls import path
from . import views  # Import the views we just made

app_name = "blog"  # This is for namespacing the URLs

urlpatterns = [
    # Example: website.com/blog/
    path("", views.PostListView.as_view(), name="list"),
    # Example: website.com/blog/my-first-post/
    # We use <slug:slug> to capture the slug from the URL
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
]
