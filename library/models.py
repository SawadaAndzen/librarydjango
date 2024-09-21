from django.db import models


class LibraryBook(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    isbn = models.CharField(max_length = 50, unique = True)
    available = models.BooleanField(default = True)
    
    class Meta:
        ordering = ['author']
        indexes = [
            models.Index(fields = ['isbn'], name = 'isbn_index')
        ]
    
    def __str__(self):
        return f'{self.title} by {self.author}'