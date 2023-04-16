from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .selenium import SeleniumData
from .models import Stats, Rekvizit

@login_required(login_url='Auth')

def Home(request):
    stats = Stats.objects.all()
    return render(request, 'home/index.html', {"stats": stats})

def Auth(request):
    error = ""
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirmpassword")
    
        if email == None :
            user= authenticate(request, username=username, password=password)
                
            if user is not None:
                login(request, user) 
                return redirect('Home')
            else:
                return render(request, 'auth/auth.html', {"notFind": "Password or username is incorrect!"})
        else:
            if password != confirmPassword:
                error= "Password mismatch"
                return render(request, 'auth/auth.html', {"error": error})
            else:
                new_user = User.objects.create_user(username,email, password)
                new_user.save()
                return redirect('Auth')
    return render(request, 'auth/auth.html', {error: error})

def AddInstagram(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "" or password == "":
            return redirect('AddInstagram')
        else:
           [followers, name, followings] = SeleniumData(username, password)
           stats = Stats.objects.all()
           if followers == "" and name == "" and followings == "":
              return render(request, 'home/addInstagram.html', {"error" : "Password or Login invalid"})
           elif len(stats) > 0:
              Stats.objects.filter(id = 1).update(followers = followers, name = name, followings = followings)
              Rekvizit.objects.filter(id = 1).update(login = username, password = password)
           else:  
              stats = Stats(followers = followers, name = name, followings = followings)
              rekviziti = Rekvizit(login = username, password = password)
              stats.save()
              rekviziti.save()
        return redirect('Home') 

    return render(request, 'home/addInstagram.html')



def Logout(request):
    logout(request)
    return redirect("auth/auth.html")