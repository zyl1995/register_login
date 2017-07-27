from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from use_profiles.forms import UserForm, UserProfileForm

def index(request):
    return render(request, 'users/index.html',{})

@csrf_exempt
def register(request):
    #if request.session.test_cookie_worked():
    #    print ">>>>>Test COOKIE WORKED"
    #    request.session.delete_test_cookie()
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and userprofile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = userprofile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']


            profile.save()

            registered = True

        else:
            print user_form.errors, userprofile_form.errors


    else:

        user_form = UserForm()

        userprofile_form = UserProfileForm()

    return render(request, 'users/register.html',
                            {'user_form':user_form,
                            'userprofile_form':userprofile_form,
                            'registered':registered
                            }
                  )

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)

                return HttpResponseRedirect('/users/')

            else:
                return HttpResponse("Your Rango account is disabled.")

        else:
            print "Invalid login details:{0},{1}".format(username,password)
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request,'users/login.html',{})


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/users/')



# Create your views here.
