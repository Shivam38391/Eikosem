from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Todo

# Register your models here.


admin.site.register(CustomUser, UserAdmin)


class TodoAdmin(admin.ModelAdmin):
    list_display = ("__str__","todo_title", "status","created_at","updated_at"
                    )
admin.site.register(Todo, TodoAdmin)
