from django.shortcuts import render, redirect
from .models import Category, Photo

# Create your views here.


def gallery(request):
    category_name = request.GET.get('category')
    print(category_name)

    if category_name == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category_name)
    
    categories = Category.objects.all()

    context = {
        'categories': categories,
        'photos': photos[::-1],
    }
    return render(request, 'photos/gallery.html', context)


def addPhoto(request):
    categories = Category.objects.all()

    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        if data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'].title
            )
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )
        print(photo.id)
        return redirect('photo', pk=photo.id)

    context = {
        'categories': categories,
    }
    return render(request, 'photos/add.html', context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {
        'photo': photo,
    }
    return render(request, 'photos/photo.html', context)
