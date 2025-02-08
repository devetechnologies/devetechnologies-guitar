from django.db import models
from base.models import BaseModel
from cloudinary.models import CloudinaryField

# Create your models here.
class Guitar(BaseModel):
    """
    Model representing a Guitar.
    """
    ACOUSTIC = 'acoustic'
    ELECTRIC = 'electric'
    BASS = 'bass'
    CLASSICAL = 'classical'
    GUITAR_TYPES = [
        (ACOUSTIC, 'Acoustic'),
        (ELECTRIC, 'Electric'), 
        (BASS, 'Bass'),
        (CLASSICAL, 'Classical'),
    ]

    brand = models.CharField(max_length=100, help_text="Brand of the guitar (e.g., Fender, Gibson).")
    model = models.CharField(max_length=100, help_text="Model name or number of the guitar.")
    type = models.CharField(max_length=20, choices=GUITAR_TYPES, help_text="Type of guitar.")
    string_count = models.PositiveSmallIntegerField(default=6, help_text="Number of strings.")
    color = models.CharField(max_length=50, null=True, blank=True, help_text="Color of the guitar.")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the guitar.")
    description = models.TextField(null=True, blank=True, help_text="Additional details about the guitar.")
    is_available = models.BooleanField(default=True, help_text="Is the guitar available for sale?")
    image = models.ImageField(upload_to='devetechnologies-images/', blank=True)
    #image = CloudinaryField('devetechnologies-images', help_text="Image of the guitar.")  # Cloudinary image field
    #image = models.FileField(upload_to='montolio-blog',null=True,blank=True,default="images/default_images.jpg")
    def __str__(self):
        return f"{self.brand} {self.model} ({self.type})"

    class Meta:
        ordering = ['brand', 'model']
        verbose_name = "Guitar"
        verbose_name_plural = "Guitars"
