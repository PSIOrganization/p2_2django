from django.db import models

class Persona(models.Model):
    """Model representing a person."""
    # persona(id, nombre, apellido, email)
    person_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        ordering = ['person_id'] # lower person_id first

    def get_absolute_url(self): # TO_DO
        """Returns the URL to access a particular person instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}, {self.surname}'
