from django.db import models

# Create your models here.
class User( models.Model ):
    first_name = models.CharField( max_length=255 )
    last_name = models.CharField( max_length=255 )
    email_address = models.CharField( max_length=255 )
    age = models.IntegerField()
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField( auto_now_add=True )
    
    def __str__( self ):
        return f"<User Object: {self.full_name()} | {self.email_address}"
    
    def full_name( self ):
        return f"{self.first_name} {self.last_name}"