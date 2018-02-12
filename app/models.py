from django.urls import reverse
from django.db import models


# Create your models here.
class Rock(models.Model):
    class Meta:
        db_table = 'rocks'
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return '%s %s' % (self.name, self.description)

    def get_absolute_url(self):
        return reverse('rocks')
