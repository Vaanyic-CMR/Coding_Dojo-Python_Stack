from django.shortcuts import render
from time import localtime, strftime

def index( request ):
    datetime = strftime("%Y-%m-%d %I:%M %p", localtime()).split()
    context = {
        "date": datetime[0],
        "time": f"{datetime[1]} {datetime[2]}",
    }
    return render(request,'index.html', context)

