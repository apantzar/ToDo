from django.db import models


# Create your models here.
class Note(models.Model):

    note_text = models.TextField(max_length=200, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.note_text
