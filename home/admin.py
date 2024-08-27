from django.contrib import admin
from .models import Contact , Profile ,CartItems ,Dishes , Cart ,DishCategory

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display =['id' ,'name','email','subject','added_on']

    
admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(Dishes)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(DishCategory)