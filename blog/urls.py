from django.urls import path
from . import views

# urlpatterns pull from the views.py
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("posts/", views.posts, name="blog_posts"),
    path("post/<int:pk>/", views.post, name="blog_post"),
    path("category/<category>/", views.category, name="blog_category"),

]