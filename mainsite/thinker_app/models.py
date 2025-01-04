from django.db import models

# Create your models here.
class Thought(models.Model):
    id = models.BigAutoField(primary_key=True)
    msg = models.CharField(verbose_name="message", max_length=255)
    img = models.ImageField(upload_to="posts",blank=True)

    def __str__(self):
        return f"Thought #{self.id}"
