from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.detail import DetailView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import AddressSerializer
from .forms import SignUpForm, CodeForm, LoginForm, CommentForm
from django.contrib import messages
from core.utils import send_otp, check_otp
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.utils.translation import gettext_lazy as _

from .models import User, Addresses


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
        if request.session.get('info', False):
            f = CodeForm()
            send_otp(request.session['info']['phone'])
            return render(request, 'customer/CodeForm.html', {'form': f})
        else:
            return redirect('core:home')
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
            return render(request, 'customer/signIn.html', {'form': f})


class Profile(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    login_url = '/login/'
    model = User
    template_name = 'customer/profile.html'

    def test_func(self):
        if str(self.request.user.id) == str(self.kwargs['pk']):
            return True
        return False


class CreateComment(View):
    def post(self, request):
        c = CommentForm(request.POST)
        if c.is_valid():
            c.save()
            messages.info(request, _('your comment after approve will be show'))
        else:
            messages.error(request, _(c.errors))
        return redirect('product:detail', pk=request.POST['object_id'])


class AddressListAPI(generics.ListCreateAPIView):
    serializer_class = AddressSerializer

    def get_queryset(self):
        return Addresses.objects.filter(is_deleted=False)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(user=kwargs['user_id']))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
