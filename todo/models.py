from django.db import models

# Create your models here.
# The below creates a new table
class Item(models.Model):
    
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)
    # The below returns the name of our to do task instead of 'Item Object' when
    # viewed from within the admin panel
    def __str__(self):
        return self.name