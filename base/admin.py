from django.contrib import admin
from .models import Freelancer, Employer, Job, Message, Level

# Register your models here.
admin.site.register(Freelancer)
admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(Message)
admin.site.register(Level)