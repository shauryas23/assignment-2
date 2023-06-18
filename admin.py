from django.contrib import admin
from .models import UserProfile
from .models import Transaction

admin.site.register(UserProfile)
admin.site.register(Transaction)