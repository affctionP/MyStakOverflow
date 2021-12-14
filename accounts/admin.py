from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm,UserCreateForm
from .models import USER
# Register your models here.
class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    form = UserChangeForm
    list_display=('email','is_superuser')
    
    fieldsets = (
        (None, {
            "fields": (
                'email','is_active','is_staff'
            ),
        }),
        ('Permissions',{
            'fields':(
            'is_superuser',
        ),
            
        }),
    )
    
    ordering = ('email',)
    
    
    
admin.site.register(USER , UserAdmin)