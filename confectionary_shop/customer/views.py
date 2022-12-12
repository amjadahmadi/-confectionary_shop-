from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView
from .models import User
from .forms import SignUpForm, CodeForm
from django.contrib import messages
from core.utils import send_otp


# Create your views here.

class UserCreateView(View):

    def get(self, request):
        f = SignUpForm()
        return render(request, 'customer/register.html', {'form': f, 'met': 'signup'})
        # template_name_suffix = 'customer/signup.html'

    def post(self, request):
        f = SignUpForm(request.POST or None)
        if f.is_valid():
            request.session['info'] = f.cleaned_data
            return redirect('user:code')
        else:
            print(f.errors)
            return render(request, 'customer/register.html', {'form': f})


class CodeGenerate(View):

    def get(self, request):
        f = CodeForm()
        send_otp(request.session['info']['phone'])
        return render(request, 'customer/CodeForm.html', {'form': f})
        # template_name_suffix = 'customer/signup.html'

    def post(self, request):
        f = SignUpForm(request.POST or None)
        if f.is_valid():

            return redirect('user:code')
        else:
            print(f.errors)
            return render(request, 'customer/register.html', {'form': f})
