from django.shortcuts import render

# Create your views here.
def authentication(request):
    return render(request, 'kitap/authentication.html')

def index(request):
    return render(request, 'kitap/index.html')

def about(request):
    return render(request, 'kitap/about.html')

def categories(request):
    return render(request, 'kitap/categories.html')

def profile(request):
    return render(request, 'kitap/profile.html')

def faq(request):
    return render(request, 'kitap/faq.html')