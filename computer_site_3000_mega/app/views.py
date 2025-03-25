from django.shortcuts import render
from .models import catalog

def catalog_shop(request):
    tovari = catalog.objects.all()
    return render(request, "catalog.html", {"products": tovari})
  
def about(request):
  return render(request, "index.html")

