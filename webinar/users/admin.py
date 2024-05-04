from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    readonly_fields = [
        "date_joined",
    ]
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Permissions"), {"fields": ("is_staff", "is_active")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

    def has_delete_permission(self, request, obj=None):
        # prevent staff users from deleting a model instance, regardless of their permissions
        return False

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()

        if not is_superuser:
            disabled_fields |= {
                "username",
                "is_superuser",
                "user_permissions",
            }

        # Prevent non-superusers from editing their own permissions
        if not is_superuser and obj is not None and obj == request.user:
            disabled_fields |= {
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form

    # ----------- Restrict Access to Custom Actions ----------- #

    actions = [
        "activate_users",
    ]

    def activate_users(self, request, queryset):
        assert request.user.has_perm("auth.change_user")
        cnt = queryset.filter(is_active=False).update(is_active=True)
        self.message_user(request, "Activated {} users.".format(cnt))

    activate_users.short_description = "Activate Users"

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.has_perm("auth.change_user"):
            del actions["activate_users"]
        return actions

    # --------------------------------------------------------- #

    # def save_related(self, request, form, formsets, change):
    #     super().save_related(request, form, formsets, change)
    #     role = formsets
    #     form.instance.roles.add(role)


admin.site.register(User, CustomUserAdmin)
