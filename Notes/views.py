from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import logout, authenticate, login

#from
# Create your views here.
def index(request):
    #return HttpResponse("Hello Welcome to Index Page!!")
    context = {
        'name': 'Umang',
        'surname': 'Mathur'
    }

    #if request.method=="POST" and 'run_script' in request.POST:
        #main_func()
    if request.user.is_anonymous:
        return render(request,'login.html')
    else:
        return render(request,'body.html',context)

def query(request):
    if request.user.is_anonymous:
        return redirect("/")
    else:
        return render(request,'query.html')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")