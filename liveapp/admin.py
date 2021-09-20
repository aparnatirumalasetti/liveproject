from django.contrib import admin
from .models import school
admin.site.register(school)

# Register your models here.
class schooladmin(admin.ModelAdmin):
    fields=['Std_name','Email','standard','mobile','Address']
    def new_content(self,obj,*args,**kwargs):
        return str(obj.std_name)
    class Meta:
        model=school
