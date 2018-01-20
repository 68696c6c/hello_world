from django.db import models


# Create your models here.
class Rock(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return '%s %s' % (self.name, self.description)
