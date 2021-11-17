from django.db.models.expressions import Value
from django.shortcuts import render, redirect
from django.contrib import messages
from . import models

# .strftime( '%B %d, %Y' )

# Create your views here.
def index( request ):
    return redirect( '/shows' )

def shows( request ):
    context = {
        'shows': models.Show.objects.all(),
    }
    return render( request, 'shows.html', context=context )

def new_show( request ):
    return render( request, 'new_show.html' )

def create_show( request ):
    errors = models.Show.objects.basic_validator( request.POST )
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error( request, value )
        return redirect( f'/shows/new')
    else:
        s = models.Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            desc = request.POST['desc']
        )
        return redirect( f'/shows/{s.id}' )

def view_show( request, show_id=None ):
    context = {
        'show': models.Show.objects.get( id=show_id )
    }
    return render( request, 'view_show.html', context=context)

def edit_show( request, show_id=None ):
    context = {
        'show': models.Show.objects.get( id=show_id )
    }
    return render( request, 'edit_show.html', context)

def update_show( request, show_id=None ):
    errors = models.Show.objects.basic_validator( request.POST )
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error( request, value )
        return redirect( f'/shows/{show_id}/edit')
    else:
        s = models.Show.objects.get( id=show_id )
        s.title = request.POST['title']
        s.network = request.POST['network']
        s.release_date = request.POST['release_date']
        s.desc = request.POST['desc']
        s.save()
        return redirect( f'/shows/{s.id}' )

def destroy( request, show_id=None ):
    s = models.Show.objects.get( id=show_id )
    s.delete()
    return redirect( '/shows' )