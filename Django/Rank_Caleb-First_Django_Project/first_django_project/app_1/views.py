from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# Create your views here.
def root( request ):
    return redirect( '/blogs' )

def index( request ):
    return HttpResponse( "placeholder to later display a list of blogs." )

def new( request ):
    return HttpResponse( "placeholder to display a new form to create a new blog" )

def create( request ):
    return redirect( '/' )

def show( request, x ):
    return HttpResponse( f"placeholder to display blog number: {x}")

def edit( request, x ):
    return HttpResponse( f"placeholder to edit blog {x}")

def destroy( request, x ):
    return redirect( '/blogs' )

def get_json( request ):
    return JsonResponse({"title": "Blog Title", "content": "Blog Content"})
