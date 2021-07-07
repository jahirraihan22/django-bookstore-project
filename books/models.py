from django.db import models

# Create your models here.


class Book (models.Model):
    title = models.CharField(max_length=256)
    # isbn = models.CharField(max_length=256)
    pageCount = models.IntegerField(default=0)
    # publishedDate = models.DateTimeField()
    thumbnailUrl = models.CharField(max_length=256, null=True)
    shortDescription = models.CharField(max_length=256, null=True)
    longDescription = models.TextField(null=True)
    # status = models.CharField(max_length=256, null=True)
    # authors = models.CharField(max_length=256, null=True)

    def __str__(self):
        # to return as title
        return self.title


class Review(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
