# admin.py
from django.contrib import admin
from .models import CustomUser, Administrator, Student, Payment, Refund

admin.site.register(CustomUser)
admin.site.register(Administrator)
admin.site.register(Student)
admin.site.register(Payment)
admin.site.register(Refund)