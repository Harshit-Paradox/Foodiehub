from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
import uuid





class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    profile_pic =models.ImageField(upload_to='profiles/%Y/%m/%d' , null=True, blank=True)
    address= models.TextField(blank=True)
    contact_number=models.CharField(max_length=15)
    updated_on= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural ="User Table"

class BaseModel(models.Model):
    uid=models.UUIDField(default=uuid.uuid4 ,editable=False , primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True

class DishCategory(BaseModel):
    category_name= models.CharField(max_length=100)

    def __str__(self):
        return self.category_name




class Dishes(BaseModel):
    category = models.ForeignKey(DishCategory , on_delete=models.CASCADE , related_name="dishes")
    Dish_name=models.CharField(max_length=100)
    Price= models.IntegerField(default=100)
    images = models.ImageField(upload_to='dish')

    def __str__(self):
        return self.Dish_name




class Cart(BaseModel):
    user = models.ForeignKey(User ,null=True ,blank=True, on_delete=models.SET_NULL , related_name="carts")
    is_paid=models.BooleanField(default=False)

    def get_cart_total(self):
        return CartItems.objects.filter(cart =self).aggregate(Sum('dish__Price'))['dish__Price__sum']



class CartItems(BaseModel):
    cart=models.ForeignKey(Cart , on_delete=models.CASCADE , related_name="cart_items")
    dish= models.ForeignKey(Dishes , on_delete=models.CASCADE)
