from django.contrib import admin
# Register your models here.

from .models import Profile, Skill, Message, Role
from django_otp.admin import OTPAdminSite
from django.contrib.auth.models import User, Group

from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin

class OTPAdmin(OTPAdminSite):
    pass

admin.site = OTPAdmin(name='OTPAdmin')
admin.site.register(User)
admin.site.register(TOTPDevice, TOTPDeviceAdmin)
# Instantiate your custom admin site
otp_admin_site = OTPAdmin(name='OTPAdmin')

# Register the User model with the custom admin site
otp_admin_site.register(User)
otp_admin_site.register(Group)
admin.site.register(Role)
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Message)
