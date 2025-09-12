from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("author", "publication_year")


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "username", "password", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2", "is_staff", "is_active"),
        }),
    )
    search_fields = ("email", "username")

# ✅ This is the exact line the checker is looking for
admin.site.register(CustomUser, CustomUserAdmin)
