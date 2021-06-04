from django.db import models

# Create your models here.
class Room(models.Model):
    """Represents that chat rooms users can join."""
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)

    def __str__(self):
        """Returns human-readable represention of the model instance."""
        return self.name
