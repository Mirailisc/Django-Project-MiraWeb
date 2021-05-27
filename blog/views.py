from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import Article
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'homepage/home.html')

class Dashboard():
    def dashboard(request):
        return render(request, 'dashboard/dashboard.html')

class auth():

    def Sign_in(request):
        return render(request, 'auth/form_sign-in.html')

    def login(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/feed')

        else:
            messages.info(request, 'Invalid username or password.')
            return redirect('/sign_in')

    def logout(request):
        logout(request)
        return redirect('/')

    def register_form(request):
        return render(request, 'auth/form-register.html')

    def register(request):
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']

        if password == repassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists.')
                return redirect('/register_form')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists.')
                return redirect('/register_form')
            else:
                user = User.objects.create(
                username=username,
                password = make_password(password),
                email=email,
                first_name=firstname,
                last_name=lastname
                )

                user.save()
                return redirect('/')

        else:
            messages.info(request, 'Password and confirm password does not match.')
            return redirect('/register_form')

class Post():
    @login_required(login_url='/sign_in')
    def feed_show(request):
        data = Article.objects.order_by('-create_date').all
        return render(request, 'Post/post_dashboard.html', {'post':data})

    def add(request):
        title = request.GET['title']
        info = request.GET['info']
        link = request.GET['link']

        post = Article.objects.create(
                article_name = title,
                articlk_info = info,
                article_link = link,
                author = request.user,
                create_date = request.user
                )

        post.save()
        return redirect('/feed')

    def delete(request, id):
        Article.objects.filter(id=id).delete()
        return redirect('/feed')

    def edit_name(request, id):
        title = request.GET['title']
        
        Article.objects.filter(id=id).update(article_name = title)
                        
        return redirect('/feed')

    def edit_info(request, id):
        info = request.GET['info']
        
        Article.objects.filter(id=id).update(articlk_info = info)
                        
        return redirect('/feed')

    def edit_link(request, id):
        link = request.GET['link']
        
        Article.objects.filter(id=id).update(article_link = link)
                        
        return redirect('/feed')

class Account():
    @login_required(login_url='/sign_in')
    def Profile(request, id):
        User.objects.filter(id=id).all
        return render(request, 'account/account.html')

    def edit_firstname(request, id):
        firstname = request.GET['firstname']
        
        User.objects.filter(id=id).update(first_name = firstname)
                        
        return redirect('/feed')

    def edit_lastname(request, id):
        lastname = request.GET['lastname']
        
        User.objects.filter(id=id).update(last_name = lastname)
                        
        return redirect('/feed')
        
    def edit_email(request, id):
        email = request.GET['email']
        if User.objects.filter(email=email).exists():
            return messages.info(request, 'This Email is taken.')

        else:
            User.objects.filter(id=id).update(email = email) 
            return redirect('/feed')

class Search():
    def show(request):
        search = request.POST['search']
        result = Article.objects.filter(
            articlk_info__contains=search
            )
        return render(request, 'Post/post_search.html', {'search':search, 'result':result})