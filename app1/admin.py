from django.contrib import admin
from app1.models import Emp
# Register your models here.

class Eadmin(admin.ModelAdmin):
    list_display=['eid','ename','esal','eemail']

admin.site.register(Emp,Eadmin)