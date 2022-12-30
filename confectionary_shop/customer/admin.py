from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile, Bank_Account, Addresses, Comment


# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('user_info', {'fields': ('phone',)}),
        ('user bank info', {'fields': ('bank_account',)}),
        ('user profile', {'fields': ('profile',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2'),
        }),
    )
    list_display = ['phone', 'first_name', 'last_name', 'is_staff']
    search_fields = ('first_name', 'last_name', 'phone')
    ordering = ('last_name',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'gender', 'birth_day']
    search_fields = ('email',)
    ordering = ('birth_day',)


@admin.register(Addresses)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['full_address', 'user']
    search_fields = ('full_address', 'user__first_name', 'user__last_name', 'user__phone')
    ordering = ('user__last_name',)


@admin.register(Bank_Account)
class BankAdmin(admin.ModelAdmin):
    list_display = ['balance', 'card_bank']
    search_fields = ('card_bank',)
    ordering = ('balance',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.get_fields()]
    search_fields = ['content_object']
    ordering = ('-id',)


admin.site.register(User, UserAdmin)
