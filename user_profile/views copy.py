from datetime import datetime
from django.shortcuts import redirect, render
from django.views import View
from product.models import ProductCategory,Product
from user_profile.forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.models import User
 
class UserProfilesView(View):
    form_class = UserProfileForm
    def get(self,request):

        form_class = self.form_class()
        navigationProductCategory = ProductCategory.objects.all()
        product =  Product.objects.filter(status=True)
        userprofile = UserProfile.objects.filter(user_id=request.user.id)
        context = {
            'UserProfileForm':form_class,
            'navigationProductCategory':navigationProductCategory,
            'product':product,
            # 'userprofile':list(userprofile.values()),
            'userprofile':userprofile,
          }
        return render(request, 'user-profile.html',context)

    def post(self,request):
        print(request.POST,request.FILES)
        user_id = request.POST.get('user_id')
        data,created = User.objects.get_or_create(id=request.user.id)
        data.first_name = request.POST.get('first_name')
        data.last_name = request.POST.get('last_name')

        userprofile_data,created = UserProfile.objects.get_or_create(user_id=request.user.id) 
       
        if request.FILES == '':
            user_imgs = request.FILES['user_img']
            print("blank")
        elif request.FILES != '':
            user_imgs = request.FILES['user_img'] 
            userprofile_data.user_img= user_imgs
            print("*******",user_imgs)

        # else:
        #     userprofile_data.user_img= user_imgs


        userprofile_data.address = request.POST.get('address')
        userprofile_data.about = request.POST.get('about')
        data.save()
        userprofile_data.save()
        return redirect("UserProfile")
