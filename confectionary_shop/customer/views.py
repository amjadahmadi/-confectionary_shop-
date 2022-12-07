from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from .models import User
from .forms import SignUpForm


# Create your views here.

class UserCreateView(View):

     def get(self, request):
        f = SignUpForm()
        return render(request, 'customer/register.html', {'form': f})
        # template_name_suffix = 'customer/signup.html'
