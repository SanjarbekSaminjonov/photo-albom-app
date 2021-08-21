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

        if data['category'] != 'none' and data['category_new'] == '':
            category = Category.objects.get(id=data['category'])

        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'].title()
            )
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )
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


def deletePhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    photo.delete()
    return redirect('gallery')


def categoryManager(request):
    msg = ''

    if request.method == 'POST':
        category_new = request.POST['category_new'].title()
        category, created = Category.objects.get_or_create(name=category_new)
        if not created:
            msg = 'It has already created!'
    
    categories = Category.objects.all()
    context = {
        'categories': categories[::-1],
        'msg': msg
    }
    return render(request, 'photos/category.html', context)


def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('category_manager')
