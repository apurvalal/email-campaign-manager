from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
