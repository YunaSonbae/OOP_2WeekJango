from django.contrib import admin
from .models import User, Application, Category


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'status', 'category')


admin.site.register(Category)
