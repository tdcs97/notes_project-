from django.contrib import admin
from .models import Note, Contact

# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title','note','date','user']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','msg']

# @admin.register(Register)
# class UserAdmin(admin.ModelAdmin):
#     fields = ('name','email','num','passwd')

# @admin.register(Login)
# class LoginAdmin(admin.ModelAdmin):
#     fields = ('username','password')