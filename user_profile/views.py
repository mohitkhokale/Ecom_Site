from django.shortcuts import render
from django.views import View
from product.models import ProductCategory
from user_profile.forms import UserProfileForm
from user_profile.models import UserProfile
from django.contrib.auth.models import User      

def UpdateUserProfile(request,pk=None):

        user = User.objects.get(id=pk)
        print('************',user.id)
        if request.user.is_authenticated():
            navigationProductCategory = ProductCategory.objects.all()
            Product_Category = UserProfile.objects.get(pk=id)
            print(Product_Category)
            form_class = UserProfileForm(request.POST or None, request.FILES or None,instance=Product_Category)
            if form_class.is_valid():
                form_class.save()   
            context ={
                'navigationProductCategory':navigationProductCategory ,
                'profile_id':Product_Category,
                'forms':form_class,
            }
            
            return render(request,"update-user-profile.html",context)


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