from django.shortcuts import render
from django.views import View
from product.models import ProductCategory
from user_profile.forms import UserProfileForm
from user_profile.models import UserProfile
from django.contrib.auth.models import User      

def UpdateUserProfile(request,pk=None):
    try:
        user = UserProfile.objects.get(pk=pk)
        if request.user.id == user.id:
            profile_id = UserProfile.objects.get(pk=pk)
            user_img = UserProfile.objects.filter(pk=pk)
            navigationProductCategory = ProductCategory.objects.all()
        
            form_class = UserProfileForm(request.POST or None, request.FILES or None,instance=profile_id)
            if form_class.is_valid():
                form_class.save()   
            context ={
                'navigationProductCategory':navigationProductCategory ,
                'profile_id':profile_id,
                'user_img':user_img,
                'forms':form_class,
            }
            
            return render(request,"update-user-profile.html",context)
        else:
            return render(request,"home-page.html", )

    except UserProfile.DoesNotExist:
        return render(request,"home-page.html", )


# class UserProfilesView(View):
#     form_class = UserProfileForm
#     def get(self, request):
#         form_class = self.form_class()
#         context = { 
#             'form':form_class,
#             # 'data':list(data.values())
#         }
#         return render(request, 'user-profile.html', context)


#     def post(self, request,id=None):
#         Product_Category = UserProfile.objects.get(id=id) 
#         form_class = UserProfileForm(request.POST or None, request.FILES or None,instance=Product_Category)
#         data = UserProfile.objects.filter(id=3)
#         if form_class.is_valid():
#             form_class.save()   
#         context ={
#             'form':form_class,
#             'data':data
#         }
        
#         return render(request,'user-profile.html',context)