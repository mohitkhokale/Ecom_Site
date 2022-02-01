from django import views
from django.shortcuts import redirect, render
from django.views import View
from product.models import ProductCategory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as AuthLogin , logout as AuthLogout
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
