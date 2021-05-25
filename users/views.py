from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CreateUserForm,UserLoginForm

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_name = form.cleaned_data.get('user_name')
        password = form.cleaned_data.get('password')
        user = authenticate(user_name=user_name, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "User/login.html", context)
def logout_view(request):
    logout(request)
   
    print(' youre logged out')
    return redirect('/')


def signup_view(request):
    form=CreateUserForm()
    if request.method == 'POST':
        print('post request done')
        form=CreateUserForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('user_name')
            messages.success(request,'Account created for ' + user)
            return redirect('login')
        
    context={'form':form}

    return render(request,'User/register.html',context)



    