from django.shortcuts import render, redirect
from .models import Category, Photo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# Create your views here.


def registerUser(request):
    form = CustomUserCreationForm

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            new_user = authenticate(
                username=user.username, password=request.POST['password1'])
            login(request, new_user)
            return redirect('gallery')

    context = {
        'form': form,
        'page': 'register',
    }
    return render(request, 'photos/loginRegister.html', context)


def loginUser(request):
    username = ''
    msg = ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('gallery')
        else:
            msg = 'Username or password is wrong!'
    context = {
        'username': username,
        'msg': msg,
        'page': 'login',
    }

    return render(request, 'photos/loginRegister.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('gallery')


@login_required(login_url='login')
def gallery(request):
    category_name = request.GET.get('category')

    if category_name == None:
        photos = Photo.objects.filter(category__author=request.user).order_by('-id')
    else:
        photos = Photo.objects.filter(
            category__name=category_name, category__author=request.user).order_by('-id')

    categories = Category.objects.filter(author=request.user)

    context = {
        'categories': categories,
        'photos': photos,
    }
    return render(request, 'photos/gallery.html', context)


@login_required(login_url='login')
def addPhoto(request):
    categories = Category.objects.filter(author=request.user)

    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none' and data['category_new'] == '':
            category = Category.objects.get(id=data['category'])

        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'].title(),
                author=request.user,
            )
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )
        return redirect('view_photo', pk=photo.id)

    context = {
        'categories': categories,
    }
    return render(request, 'photos/addPhoto.html', context)


@login_required(login_url='login')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {
        'photo': photo,
    }
    return render(request, 'photos/viewPhoto.html', context)


def editPhoto(request, pk):
    categories = Category.objects.filter(author=request.user)
    photo = Photo.objects.get(id=pk)

    if request.method == "POST":
        description = request.POST['description']
        category_id = request.POST['category']
        category_name_new = request.POST['category_new'].title()
        if category_name_new != '':
            category, created = Category.objects.get_or_create(
                name=category_name_new,
                author=request.user
            )
        elif category_id != 'none':
            category = Category.objects.get(id=category_id)
        photo.description = description
        photo.category = category
        photo.save()
        return redirect('view_photo', pk=photo.id)

    context = {
        'categories': categories,
        'photo': photo,
    }
    return render(request, 'photos/editPhoto.html', context)


def deletePhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    photo.delete()
    return redirect('gallery')


@login_required(login_url='login')
def categoryManager(request):
    msg = ''
    category = ''

    if request.method == 'POST':
        category_new = request.POST['category_new'].title()
        category, created = Category.objects.get_or_create(
            name=category_new,
            author=request.user
        )
        if not created:
            msg = 'It has already created!'
        else:
            category = ''

    categories = Category.objects.filter(author=request.user).order_by('-id')
    context = {
        'categories': categories,
        'msg': msg,
        'category': category,
    }
    return render(request, 'photos/categoryManager.html', context)


def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('category_manager')
