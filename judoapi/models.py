from django.db import models

class Techniques(models.Model):
    name = models.CharField(max_length=60)
    img = models.CharField(max_length=500)

    def __str__(self):
        return self.name