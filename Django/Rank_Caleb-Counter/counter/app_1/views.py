from django.shortcuts import redirect, render

# Create your views here.
def index( request ):
    if 'count' not in request.session:
        request.session['count'] = 0
    
    request.session['count'] += 1
    return render( request, 'counter.html' )

def add( request ):
    
    request.session['count'] += int(request.POST['add_by'])
    return redirect( '/' )

def destroy_session( request ):
    request.session.clear()
    return redirect( '/' )