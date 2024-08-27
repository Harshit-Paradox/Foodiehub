from django.shortcuts import render , redirect ,HttpResponse , get_object_or_404
from .models import *
from django.shortcuts import redirect, HttpResponse, render
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ContactForm
from home.models import Profile


def index(request):
   return render(request,"index.html")

def home(request):
   return render(request,"index.html")

def about(request):
   return render(request,"about.html")

def service(request):
   return render(request,"service.html")   

def menu(request):
   return render(request,"menu.html")   

def recepie(request):
   return render(request,"recepie.html")   

from django.contrib.auth.decorators import login_required



def onlineorder(request):

    if not request.user.is_authenticated:
        # Redirect to index page with a query parameter to trigger the login modal
        return redirect('/?next=/onlineorder/')

    dishes = Dishes.objects.all()
    context = {'dishes': dishes}
    return render(request, "dish.html", context)


def onlineorder(request):
    dishes = Dishes.objects.all()
    context = {'dishes' : dishes}
    return render(request,"dish.html" , context)

def profile(request):
    context={}

    return render(request,"profile.html",context) 

def booktable(request):
   return render(request,"booktable.html")   

def add_cart(request , dish_uid):
    user = request.user
    dish_obj= Dishes.objects.get(uid=dish_uid)

    cart , _ = Cart.objects.get_or_create(user=user , is_paid=False)

    cart_items=CartItems.objects.create(
               cart=cart,
               dish=dish_obj
        )
    

    return redirect('onlineorder')


def cart(request):
    cart=Cart.objects.get(is_paid=False,user=request.user)
    
    # response = api.payment_request_create(
    #     amount = cart.get_cart_total(),
    #     purpose ="order",
    #     buyer_name = request.user.username,
    #     email = request.user.email,
    #     redirect_url = "http://127.0.0.1:8000/success/"
    # )
    context= {'carts':cart }
    return render(request,'cart1.html',context)


def remove_cart_items(request,cart_item_uid):
    try:
        CartItems.objects.get(uid= cart_item_uid).delete()

        return redirect('cart')
    except Exception as e:
        print(e)


# from instamojo_wrapper import Instamojo
# from django.conf import settings
# api = Instamojo(api_key=settings.API_KEY,
#                 auth_token=settings.AUTH_TOKEN , endpoint="https://test.instamojo.com/api/1.1/")



# def process_payment(request):


    


from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

def success_view(request):
    messages.success(request, "We will contact you shortly")
    return render(request, 'success.html')

def handleSignup(request):
    if request.method =='POST' :
        if User.objects.filter(username__iexact=request.POST['user_name']).exists():
            return HttpResponse("User already exists")
        
        username = request.POST['user_name']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email= request.POST['email']
        pass1= request.POST['password']
        pass2= request.POST['pass2']
        contact=request.POST['phone_number']

        if (len(username)>10):
            messages.success(request, "Your Username is not Valid")
            return redirect('home')
        
        if not username.isalnum():
            messages.success(request, "Your Username is not Valid")
            return redirect('home')
        
        if pass1!=pass2:
            messages.success(request, "Your password doesnot match")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()

        profile= Profile(user=myuser,contact_number = contact)
        profile.save()


        messages.success(request, "Your Account is Created")
        return redirect('home')
    else:
        return HttpResponse('404-Notfound')
     

def handleLogin(request):
    if request.method=="POST":
        user_name=request.POST.get('loginusername')
        password=request.POST.get('loginpassword')

        user=authenticate(username= user_name, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")


def handleLogout(request):
    logout(request)
    messages.success(request, "Your Account is Logged Out")
    return redirect('home')    









































# # Create your views here.
# def receipes(request):
#     if request.method == "POST":
#       data = request.POST
      
#       receipe_image = request.FILES.get('receipe_image')
#       receipe_name= data.get('receipe_name')
#       receipe_description = data.get('receipe_description')

     
#       Receipe.objects.create(
#         receipe_image=receipe_image,
#         receipe_name=receipe_name,
#         receipe_description= receipe_description,
#         )
      
#       return redirect('/recepies') 
#     queryset = Receipe.objects.all()
#     context = {'receipes': queryset}

#     return render(request, 'receipes.html',context)

# def delete_receipe(request , id):
#    queryset = Receipe.objects.get(id=id)
#    queryset.delete()
   
#    return redirect('/recepies')
