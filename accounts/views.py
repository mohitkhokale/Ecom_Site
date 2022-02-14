from django import views
from django.shortcuts import redirect, render
from django.views import View
from product.models import ProductCategory
from django.contrib.auth.forms import AuthenticationForm
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
    return redirect("Homepage")

 
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
 
            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            AuthLogin(request, user)
 
            # redirect user to home page
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})