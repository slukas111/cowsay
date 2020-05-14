from django.db import models

# Create your models here.
class TextInput(models.Model):
    cowsay_text = models.CharField(max_length=50)

    def __str__(self):
        return self.cowsay_text