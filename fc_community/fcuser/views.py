from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Fcuser
from .forms import LoginForm, RegisterForm
# Create your views here.

def home(request):
    user_id = request.session.get('user')
    
    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)
    return HttpResponse('HOME')

def logout(request):
    if request.session.get('user') :
        print(request.session['user'])
        del(request.session['user'])
    return redirect('/')
        

def login(request):
    if request.method == 'POST' :
        form = LoginForm(request.POST)
        # print(form)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else :
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})

    
def register(request):
    if request.method == 'POST' :
        form = RegisterForm(request.POST)
        if form.is_valid():
            return redirect('/fcuser/login/')
    else : 
        form = RegisterForm()
        
    return render(request, 'register.html', {'form': form})
