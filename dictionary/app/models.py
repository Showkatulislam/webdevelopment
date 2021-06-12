from django.db import models

# Create your models h
class Word(models.Model):
    Word=models.CharField(max_length=100)
    Bangli_word=models.CharField(max_length=200)
    Arobi_word=models.CharField(max_length=200)
    def __str__(self):
        return str(f"{self.Word}")