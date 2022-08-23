from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from new_admin.models import Event, Tournaments
from . forms import TournamentsForm
from . models import TournamentApply
from new_admin.models import Winner


def index(request):
    return render(request,'index.html')
def aboutus(request):
    return render(request,'aboutus.html')
def gallery(request):
    return render(request,'gallery.html')


@login_required(login_url='login')
def home(request):
    college = User.objects.get(username=request.user.username)
    tournamentapply = TournamentApply.objects.filter(college=college)
    return render(request,'college/home.html',{'tournamentapply':tournamentapply})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'college/login.html')
    else:
        return render(request, 'college/login.html')


@login_required(login_url='login')
def admin_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def add_tournament(request):
    event = Event.objects.all()
    if request.method == 'POST':
        college = User.objects.get(username=request.user.username)
        eventname = request.POST['event']
        event = Event.objects.get(name=eventname)
        date = request.POST['date']
        level = request.POST['level']
        gender = request.POST['gender']
        tournament = Tournaments.objects.create(college=college,event=event,date=date,level=level,category=gender)
        tournament.save()
        return redirect('home')
    else:
        return render(request, 'college/addtournament.html',{'event':event})

@login_required(login_url='login')
def tournament(request):
    tournament = Tournaments.objects.all().exclude(college=User.objects.get(username=request.user))
    return render(request, 'college/tournaments.html', {'tournament':tournament})


@login_required(login_url='login')
def results(request):
    results = Winner.objects.all()
    return render(request, 'college/results.html', {'results':results})



@login_required(login_url='login')
def apply(request, id):
    tournament = Tournaments.objects.get(id = id)
    college = User.objects.get(username=request.user.username)
    tournamentapply = TournamentApply()
    tournamentapply.tournament = tournament
    tournamentapply.college = college
    tournamentapply.save()
    return redirect('home')







