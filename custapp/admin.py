from django.contrib import admin
from custapp.models import Cust
class AdminCust(admin.ModelAdmin):
    class Meta:
        models=Cust
        fields='__all__'
admin.site.register(Cust,AdminCust)

# Register your models here.
