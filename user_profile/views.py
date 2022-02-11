from django.shortcuts import redirect, render
from django.views import View
from product.models import ProductCategory,Product
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfiles(View):
        
    def get(self,request):
        navigationProductCategory = ProductCategory.objects.all()
        product =  Product.objects.filter(status=True)
        userprofile = UserProfile.objects.filter()
        context = {
            'navigationProductCategory':navigationProductCategory,
            'product':product,
            #  'userprofile':list(userprofile.values()),
          }
        return render(request, 'user-profile.html',context)

    def post(self,request):
        print(request.POST)
        user_id = request.POST.get('user_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        about = request.POST.get('about')
        print(first_name,last_name,about,user_id)
        data,created = UserProfile.objects.get_or_create(user_id=request.user.id)
        data.save()
       


        return redirect("UserProfile")