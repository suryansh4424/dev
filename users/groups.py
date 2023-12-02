# users/groups.py

from django.contrib.auth.models import Group

def create_groups():
    group_names = [
        'Executive Leadership Team',
        'Senior Management',
        'Middle Management',
        'Team Leaders',
        'Professional Staff and Specialists',
        'Front-line Employees',
    ]

    for group_name in group_names:
        Group.objects.get_or_create(name=group_name)

# Call the function to create groups
create_groups()
