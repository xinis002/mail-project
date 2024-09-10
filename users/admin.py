from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["email", "is_staff", "is_superuser"]
    ordering = ["email"]
    search_fields = ["email"]
    fieldsets = (
        (
            None,
            {"fields": ("email", "password", "phone", "city", "avatar", "is_verified")},
        ),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                    "is_active",
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
