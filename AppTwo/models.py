from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=63, unique=True)
    last_name = models.CharField(max_length=63)
    email = models.EmailField()

    def __str__(self):
        return '{} {} ({})'.format(self.first_name, self.last_name, self.email)
