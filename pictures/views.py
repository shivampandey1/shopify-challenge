from django.shortcuts import render
from .models import Category, Photo

# Create your views here.

def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name = category)
        
    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'pictures/gallery.html', context)

def viewPicture(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'pictures/picture.html', {'photo': photo})

def uploadPicture(request):
    return render(request, 'pictures/upload.html')