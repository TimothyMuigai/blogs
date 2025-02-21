from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Blog, Subscriber
from django.contrib import messages
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
# Create your views here.

def home(request):
    context = {'msg':'Welcome!'}
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def display_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html',{'blogs': blogs})

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe')
    return render(request, 'subscribe.html')

@login_required
def create_blog(request):   
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('display_blogs')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BlogForm()

    return render(request, 'create_blog.html', {'form': form})

@login_required
def delete_blog(request, blogID):
    Blog.objects.get(id = blogID).delete()
    messages.success(request, 'Blog is deleted!')
    return redirect('display_blogs')

@login_required
def edit_blog(request, pk, template_name='create_blog.html'):
    blog= get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('display_blogs')
    else:
        form = BlogForm(instance=blog)
    return render(request, template_name, {'form':form})

def cancel_action():
    return redirect('display_blogs')

def error_404(request, exception):
    return render(request, '404.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired URL name
        else:
            error_message = "Invalid credentials"
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})