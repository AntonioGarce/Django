from django.shortcuts import render, redirect
from .forms import UserForm
from .models import UserProfile
from django.contrib.auth import login
from .handler import generate_secure_code
# Create your views here.


def register(request):
    if request.method == 'POST':

        if request.POST['action'] == 'Обновить':
            return redirect("register")

        elif request.POST['action'] == 'Продолжить':
            form = UserForm(request.POST)

            if form.is_valid():
                form.cleaned_data['secure_code'] = generate_secure_code()
                user = form.save(commit=False)
                user.secure_code = generate_secure_code()
                user.save()
                login(request, user)
                return redirect('secure_code')

    else:
        form = UserForm()

    return render(request, './login/register_form.html', {'form': form})


def secure_code(request):
    if request.method == 'POST':

        return redirect('choose_city')

    return render(request, './login/secure_code.html')


def choose_city(request, ):
    if request.method == 'POST':

        if request.POST['action'] == 'Сохранить':
            user = UserProfile.objects.get(id=request.user.id)
            user.city = request.POST['city_id']
            user.save()
            return redirect('index')

        elif request.POST['action'] == 'Пропустить шаг':
            return redirect('index')

    return render(request, './login/choose_city.html')







