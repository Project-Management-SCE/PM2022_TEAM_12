from django.contrib import admin
from project.models import User,Driver,Updates
#,Passenger,Driver
# Register your models here.


admin.site.register(User)
#admin.site.register(Passenger)
admin.site.register(Driver)
admin.site.register(Updates)