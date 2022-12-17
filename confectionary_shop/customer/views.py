from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView, FormView
from .models import User
from .forms import SignUpForm, CodeForm, LoginForm
from django.contrib import messages
from core.utils import send_otp, check_otp
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class UserCreateView(View):

    def get(self, request):
        if request.user.is_authenticated and not request.user.is_superuser:
            return redirect('core:home')
        f = SignUpForm()
        return render(request, 'customer/register.html', {'form': f, 'met': 'signup'})
        # template_name_suffix = 'customer/signup.html'

    def post(self, request):
        f = SignUpForm(request.POST or None)
        if f.is_valid():
            request.session['info'] = f.cleaned_data
            return redirect('user:code')
        else:
            return render(request, 'customer/register.html', {'form': f})


class CodeGenerate(View):

    def get(self, request):
        if request.session.get('info',False):
            f = CodeForm()
            send_otp(request.session['info']['phone'])
            return render(request, 'customer/CodeForm.html', {'form': f})
        else:
            return  redirect('core:home')
        # template_name_suffix = 'customer/signup.html'

    def post(self, request):
        f = CodeForm(request.POST or None)
        if f.is_valid():
            if check_otp(request.session['info']['phone'], f.cleaned_data['valid_code']):
                user = SignUpForm(request.session['info'])
                user = user.save()
                del request.session['info']
                login(request, user)
                return redirect('core:home')
            return redirect('user:code')
        else:
            print(f.errors)
            return render(request, 'customer/register.html', {'form': f})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('core:home')


class Login(View):
    def get(self, request):

        if request.user.is_authenticated and not request.user.is_superuser:

            return redirect('core:home')

        f = LoginForm()
        x = request.GET.get('next', None)
        return render(request, 'customer/signIn.html', {'form': f, 'type': 'log', 'next': x})

    def post(self, request):
        f = LoginForm(request.POST or None)

        if f.is_valid():
            user = authenticate(request, phone=f.cleaned_data['phone'], password=f.cleaned_data['password'])

            next1 = request.GET['next']


            if user:
                login(request, user)
                if next1 != str(None):
                    return redirect(next1)
                return redirect('core:home')
            else:
                messages.error(request, 'no user')
                return redirect('user:login')

        else:
            del request.session['next']
            return render(request, 'customer/signIn.html', {'form': f})


class Profile(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return HttpResponse(request.user.first_name)
