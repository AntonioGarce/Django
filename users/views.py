from .forms import LoginForm, CapForm
from django.contrib import messages
from django.contrib.auth import logout
from .register_line import *
# Create your views here.


def first_captcha(request):
    if request.method == 'POST':

        if request.POST['action'] == 'Подтвердить':
            form = CapForm(request.POST)
            if form.is_valid():
                return redirect('login')
        elif request.POST['action'] == 'Обновить':
            return redirect("first_captcha")
    else:
        form = CapForm()
    return render(request, './login/capcha_begin.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        if request.POST['action'] == 'Обновить':
            return redirect("login")
        elif request.POST['action'] == 'Войти':
            form = LoginForm(request.POST)
            if form.is_valid():

                user = UserProfile.objects.get(username=form.cleaned_data['login'])
                if user is not None:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.error(request, 'Пользователь с таким логином нет')
    else:
        form = LoginForm()

    return render(request, './login/login_form.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('login')
