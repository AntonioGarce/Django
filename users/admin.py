from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Dispute)
admin.site.register(Dialogs)
admin.site.register(Orders)
admin.site.register(Favourite)
admin.site.register(Ticket)

