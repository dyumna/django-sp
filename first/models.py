from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    first_pub_date = models.DateTimeField('first published', auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.first_pub_date}"

