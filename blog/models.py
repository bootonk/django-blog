from django.db import models
from tinymce.models import HTMLField

# models create the tables within the database to store and read all content
class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories" # updates categorys to categories with str overide below

    def __str__(self):
        return self.name # overrides the default admin text with proper name

class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, default="", blank=True)
    body = HTMLField(blank=True, default="") # the HTML field allows for the HTML from the WISIWIG editor to work
    notes = HTMLField(blank=True, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title # overrides the default admin text with proper name

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'" # overrides the default text with proper name
