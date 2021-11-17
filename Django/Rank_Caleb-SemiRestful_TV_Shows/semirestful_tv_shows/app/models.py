from django.db import models

# Create your models here.
class ShowManager( models.Manager ):
    def basic_validator( self, data ):
        errors = dict()
        
        if len(data['title']) < 2:
            errors['title'] = "Title should be at least 2 characters."
        if len(data['network']) < 3:
            errors['network'] = "Network name should be at least 3 characters"
        if len(data['desc']) != 0:
            if len(data['desc']) < 10:
                errors['desc'] = "Description (if present) should be at least 10 characters"
        
        return errors

class Show( models.Model ):
    title = models.CharField( max_length=255 )
    network = models.CharField( max_length=255 )
    release_date = models.DateField( max_length=255 )
    desc = models.TextField( null=True )
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField( auto_now=True )
    
    objects = ShowManager()