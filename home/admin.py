from django.contrib import admin
from .models import Userform,blogcomment,Event,Notification

# Register your models here.
admin.site.register(Userform)
admin.site.register(blogcomment)
admin.site.register(Event)
admin.site.register(Notification)



