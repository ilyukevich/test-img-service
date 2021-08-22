from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission
from apps.accountapp.models import User


class Command(BaseCommand):
    """Base command for load data into database"""

    help = '>>> Load data into database (creating groups and permissions for them, creating superuser, ' \
           'creating users and selecting groups for them)'
    print(help)

    def handle(self, *args, **kwargs):
        """Base command for load data into database (creating groups and permissions for them, creating superuser,
        creating users and selecting groups for them)"""

        groups_ = ['Administrators', 'Users']

        all_permission_list = (
            'Can add User', 'Can change User', 'Can delete User', 'Can view User',
            'Can add log entry', 'Can change log entry', 'Can delete log entry', 'Can view log entry',
            'Can add group', 'Can change group', 'Can delete group', 'Can view group',
            'Can add permissions', 'Can change permissions', 'Can delete permissions', 'Can view permissions',
            'Can add category', 'Can change category', 'Can delete category', 'Can view category',
            'Can add image', 'Can change image', 'Can delete image', 'Can view image',
        )

        permission_administrator_list = (
            'Can add User', 'Can change User', 'Can delete User', 'Can view User',
            'Can add group', 'Can change group', 'Can delete group', 'Can view group',
            'Can add permissions', 'Can change permissions', 'Can delete permissions', 'Can view permissions',
            'Can add category', 'Can change category', 'Can delete category', 'Can view category',
            'Can add image', 'Can change image', 'Can delete image', 'Can view image',
        )

        permission_user_list = (
            'Can view User',
            'Can add category', 'Can change category', 'Can view category',
            'Can add image', 'Can change image', 'Can view image',
        )

        # getting a list of permissions
        permission_administrators = Permission.objects.filter(name__in=permission_administrator_list)
        permission_users = Permission.objects.filter(name__in=permission_user_list)

        # creating groups and permissions for them
        for group in groups_:
            if group == 'Administrators':
                new_group = Group.objects.create(name=group)
                print("Creation of the 'Administrators' group...OK")
                new_group.permissions.add(*permission_administrators)
                print("Create permissions for the 'Administrators' group...OK")
                new_group.save()
            elif group == 'Users':
                new_group = Group.objects.create(name=group)
                print("Creation of the 'Users' group...OK")
                new_group.permissions.add(*permission_users)
                print("Create permissions for the 'Users' group...OK")
                new_group.save()

        # creating superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(username='admin', password='admin')
            print('Create superuser...OK')

        # creating users and selecting groups for them
        administrator = User.objects.create_user(username='administrator', password='administrator',
                                                 email='administrator@img-service.com', role='Administrator', is_staff=True)
        user = User.objects.create_user(username='user', password='user',
                                        email='user@img-service.com', role='User')
        administrator.save()
        user.save()

        print('Create users...OK')

        group_administrators = Group.objects.get(name='Administrators')
        group_users = Group.objects.get(name='Users')

        # assigning users to groups
        administrator.groups.add(group_administrators)
        user.groups.add(group_users)
        print('Assigning users to groups...OK')
