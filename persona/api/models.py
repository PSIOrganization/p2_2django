from django.db import models

class Persona(models.Model):
    """Model representing a person."""
    # persona(id, nombre, apellido, email)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        ordering = ['id'] # lower id first

    def get_absolute_url(self): # TO_DO
        """Returns the URL to access a particular person instance."""
        return reverse('personas', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}, {self.surname}'
