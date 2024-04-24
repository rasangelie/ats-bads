from django.contrib import admin
from .models import Ticket, JobPosition, Comment, TechStack

# Register your models here.
admin.site.register(Ticket)
admin.site.register(JobPosition)
admin.site.register(Comment)
admin.site.register(TechStack)