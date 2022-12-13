from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from . models import Place
from . models import Name
def demo(request):
    obj=Place.objects.all()
    obj2=Name.objects.all()
    return render(request,'index.html', {"result": obj,"results":obj2})





