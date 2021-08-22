from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group, Permission
from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'role', 'last_login', 'is_staff', 'is_active',)
    search_fields = ('role', 'username',)
    list_filter = ('username', 'role', 'last_login', 'is_staff', 'is_active')
    empty_value_display = '-пусто-'
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'role', 'password1',
                       'password2',
                       ),
        }),
    )


class GroupAdminWithCount(GroupAdmin):
    """Class is representation of a model Group in the admin interface"""

    list_display = GroupAdmin.list_display + ('user_count',)

    @staticmethod
    def user_count(obj):
        """Count the number of users in a group"""

        return obj.user_set.count()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Group, GroupAdminWithCount)
