from django.contrib import admin
from django.contrib.auth.models import User, Group
# Register your models here.
from .models import Project, Review, Tag
from django_otp.admin import OTPAdminSite

from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin

class POTPAdmin(OTPAdminSite):
    pass

admin.site = POTPAdmin(name='OTPAdmin')
admin.site.register(User)
admin.site.register(TOTPDevice, TOTPDeviceAdmin)
# Instantiate your custom admin site
p_otp_admin_site = POTPAdmin(name='OTPAdmin')

# Register the User model with the custom admin site
p_otp_admin_site.register(User)
p_otp_admin_site.register(Group)
p_otp_admin_site.register(Project)
p_otp_admin_site.register(Review)
p_otp_admin_site.register(Tag)
