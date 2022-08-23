from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Event, Tournaments
from college.models import TournamentApply
from . forms import WinnerForm

@login_required(login_url='adminlogin')
def admin_home(request):
    if request.user.is_superuser:
        tournamentapply = TournamentApply.objects.all()
        return render(request,'adminhome.html',{'tournamentapply':tournamentapply})
    else:
        return render(request, 'login.html')



def admin_login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('adminhome')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


@login_required(login_url='adminlogin')
def admin_logout(request):
    logout(request)
    return redirect('adminlogin')

@login_required(login_url='adminlogin')
def add_college(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            if password == password2:
                user = User.objects.create_user(username= name, email=email, password=password)
                user.save()
                return redirect('adminhome')
        else:
            return render(request,'addcollege.html')
    else:
        return render(request, 'login.html')


@login_required(login_url='adminlogin')
def colleges(request):
    if request.user.is_superuser:
        users = User.objects.all().exclude(is_superuser=True)
        return render(request,'colleges.html',{'users':users})
    else:
        return render(request, 'login.html')
    

@login_required(login_url='adminlogin')
def tournaments(request):
    if request.user.is_superuser:
        tournaments = Tournaments.objects.all()
        return render(request,'tournaments.html',{'tournaments' : tournaments})
    else:
        return render(request, 'login.html')


@login_required(login_url='adminlogin')
def addevents(request):
    if request.user.is_superuser:
        if request.method == "POST":
            name = request.POST['name']
            players = request.POST['player']
            events = Event()
            events.name = name
            events.players = players
            events.save()
            return redirect('adminhome')
        else:
            return render(request,'addevents.html')
    else:
        return render(request, 'login.html')


@login_required(login_url='adminlogin')
def addwinner(request):
    if request.user.is_superuser:
        form = WinnerForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid:
                form.save()
                return redirect('adminhome')
        else:
            return render(request,'addwinner.html', {'form':form})
    else:
        return render(request, 'login.html')

