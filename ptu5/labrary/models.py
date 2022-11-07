from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField('name', max_length =200, help_text="Enter the name of the Genre")

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField("first name", max_length=50)
    last_name = models.CharField("Last name", max_length=50)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering =['last_name', 'first_name']
    
