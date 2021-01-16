from django.shortcuts import render

# Create your views here.
def index(request):
    liste=[]

    return render(request,"movie_rec/index.html")