from django.db import models


class Post(models.Model):

    CATEGORY_CHOICES = [
        ('romance', 'Romance'),
        ('books', 'Books & Reading'),
        ('thriller', 'Thriller & Mystery'),
        ('lifestyle', 'Lifestyle'),
        ('personal', 'Personal Stories'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default='personal'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title