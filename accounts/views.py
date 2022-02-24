from django import views
from django.shortcuts import redirect, render
from django.views import View
from product.models import ProductCategory
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth import login as AuthLogin , logout as AuthLogout
from django.contrib.auth import authenticate
from .forms import SignUpForm

# Create your views here.
class Login(View):
    template_name='login.html'
    form_class= AuthenticationForm
    navigationProductCategories = ProductCategory.objects.filter(status=True)

    def get(self,request):
        form = self.form_class()
        navigationProductCategories = ProductCategory.objects.filter(status = True)
        context = {
            'navigationProductCategory':navigationProductCategories,
            'form':form
        }

        return render(request,self.template_name,context)
        
    def post(self,request):
        form = self.form_class(data = request.POST)
        if form.is_valid():
            AuthLogin(request,form.get_user())
            return redirect('Homepage')
        
        context = {
            'navigationProductCategory':self.navigationProductCategories,
            'form':form
        }
        return render(request,self.template_name,context)
        
def logout(request):
    AuthLogout(request)
    return redirect("home")

''' USER REGISTRATION WITH PROFILE '''

def home_view(request):
    return render(request,'home-page.html')

def signup_view(request):

    form = SignUpForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.UserProfile.first_name = form.cleaned_data.get('first_name')
        user.UserProfile.last_name = form.cleaned_data.get('last_name')
        user.UserProfile.email = form.cleaned_data.get('email')
        user.UserProfile.about = form.cleaned_data.get('about')
        user.UserProfile.dob = form.cleaned_data.get('dob')
        user.UserProfile.address = form.cleaned_data.get('address')
        user.UserProfile.user_img = form.cleaned_data.get('user_img')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        AuthLogin(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})


# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  
#             # load the profile instance created by the signal
#             user.save()
#             raw_password = form.cleaned_data.get('password1')
 
#             # login user after signing up
#             user = authenticate(username=user.username, password=raw_password)
#             AuthLogin(request, user)
 
#             # redirect user to home page
#             return redirect('/')
#     else:
#         form = SignUpForm()
#     return render(request, 'register.html', {'form': form})


