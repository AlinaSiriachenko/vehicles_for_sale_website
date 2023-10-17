from django.shortcuts import render
from django.views.generic.list import ListView


from .models import *



def index(request):
    context = {
        'last_cars': Car.objects.all()[:4],
    }
    print(context)
    return render(request, 'main/index.html', context)



def about(request):
    return render(request, 'main/about.html')



class CarListView(ListView):
    model = Car
    context_object_name = 'cars'



def car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    car.views += 1
    car.save()
    context = {
        'car': car,
    }
    return render(request, 'main/car_detail.html', context)



def contacts(request):
    return render(request, 'main/contacts.html')



def manufacturer_detail(request):
    return render(request, 'main/manufacturer_detail.html')




