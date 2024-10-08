from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile , Dweet
# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)
admin.site.register(Dweet)