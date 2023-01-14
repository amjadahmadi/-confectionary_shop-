from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.detail import DetailView
from rest_framework import generics, status
from .serializers import *
from .forms import SignUpForm, CodeForm, LoginForm, CommentForm
from django.contrib import messages
from core.utils import send_otp, check_otp
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Addresses, Profile
from rest_framework import viewsets
from rest_framework import mixins


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
            print(type(next1))
            if user:
                login(request, user)
                if next1 != 'None':
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


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': f'{request.user.phone}'}
        return Response(content)


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


class AddressAPI(viewsets.ViewSet):
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Addresses.objects.filter(is_deleted=False, user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201)

    def auth(self, pk):
        instance = Addresses.objects.select_related('user').get(id=pk)
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user == instance.user:
            return instance
        return False

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):

        if instance := self.auth(pk):
            serializer = self.serializer_class(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        return Response(status=401)

    def destroy(self, request, pk=None):
        if instance := self.auth(pk):
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=401)


class ProfileAPI(viewsets.ViewSet):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Profile.objects.filter(is_deleted=False)

    def create(self, request, *args, **kwargs):
        return Response(status=404)

    def auth(self, pk):
        instance = User.objects.select_related('profile').get(id=pk)
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user == instance:
            return instance
        return False

    def retrieve(self, request, pk=None):
        if item := self.auth(pk):
            serializer = self.serializer_class(item.profile)
            return Response(serializer.data)
        return Response(status=401)

    def partial_update(self, request, pk=None):
        if instance := self.auth(pk):
            serializer = self.serializer_class(instance.profile, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        return Response(status=401)

    def destroy(self, request, pk=None):
        return Response(status=404)


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserAPI(viewsets.ViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return User.objects.all()

    def auth(self, pk):
        instance = User.objects.get(id=pk)
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user == instance:
            return instance
        return False

    def retrieve(self, request, pk=None):
        if item := self.auth(pk):
            # item = get_object_or_404(self.get_queryset(), pk=pk)
            serializer = self.serializer_class(item)
            return Response(serializer.data)
        return Response(status=401)

    def partial_update(self, request, pk=None):
        if instance := self.auth(pk):
            serializer = self.serializer_class(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        return Response(status=401)


class BankAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BankSerializer

    def auth(self, pk):
        instance = User.objects.select_related('bank_account').get(id=pk)
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user == instance:
            return instance
        return False

    def get(self, request):
        pk = request.data.get('pk')
        if item := self.auth(pk):
            serializer = self.serializer_class(item.bank_account)
            return Response(serializer.data)
        return Response(status=401)

    def put(self, request):
        pk = request.data.get('pk')
        amount = float(request.data.get('amount'))
        if int(request.user.id) == int(pk):
            user = User.objects.select_related('bank_account').get(id=pk)
            bank_account = user.bank_account
            bank_account_balance = user.bank_account.balance

            if request.data.get('type') == 'deposit':
                bank_account.balance += amount
            else:
                if bank_account_balance - amount >= 0:
                    bank_account.balance -= amount
                else:
                    return Response(status=400)
            bank_account.save()
            return Response(status=200)
        return Response(status=401)

    def patch(self, request):
        print(request.data.get('pk'))
        if item := self.auth(request.data.get('pk')):
            bank_account = item.bank_account
            bank_account.card_bank = request.data.get('card_bank')
            bank_account.save()
            return Response(status=200)
        return Response(status=401)

