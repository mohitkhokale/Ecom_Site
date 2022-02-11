from django.shortcuts import render
from django.views import View
from product.models import ProductCategory,Product,ProductImages


class HomePage(View):
    def get(self,request):
        navigationProductCategory = ProductCategory.objects.filter(status=True)
        productCategories = ProductCategory.objects.filter(status=True).order_by('-id')[:3]
        print(productCategories)

        context ={ 
            'navigationProductCategory':navigationProductCategory,
            'productCategories':productCategories,
        }
        return render(request,"home-page.html",context)

class ProductListing(View):
    template_name = 'ProductListing.html'

    def get(self,request,product_category_id=None):
 
        navigationProductCategory = ProductCategory.objects.filter(status=True)

        searchDict={"status":True}
        # products = Product.objects.filter(**searchDict)

        if product_category_id:
            searchDict['product_category_id']=product_category_id

        if request.GET.get('search'):
            searchDict['name__icontains']= request.GET.get('search')
       
        if request.GET.get('min'):
            searchDict['price__gte']= request.GET.get('min').replace('₹','')
        
        if request.GET.get('max'):
            searchDict['price__lte']= request.GET.get('max').replace('₹','')
  

        if request.GET.get("sorting"):
            if request.GET.get("sorting") == 'low':
                products = Product.objects.filter(**searchDict).order_by('price')
            if request.GET.get("sorting") == 'high':
                products = Product.objects.filter(**searchDict).order_by('-price')
        else:
            products = Product.objects.filter(**searchDict)


        context = {
            'navigationProductCategory':navigationProductCategory,
            "products":products 
        }
        return render(request,self.template_name,context)



class ProductDetails(View):
    template_name = "product-details.html"
    def get(self,request,product_id):
        navigationProductCategory = ProductCategory.objects.filter(status=True)
        try:
            product = Product.objects.get(pk=product_id)
            realtedproducts = Product.objects.filter(status=True,product_category=product.product_category.id).exclude(id=product_id)
            print(realtedproducts)
        except Product.DoesNotExist:
            product = {}
        productImages = ProductImages.objects.filter(product_id=product_id)
        context ={ 
            'navigationProductCategory':navigationProductCategory,
            'product':product,
            'productImages':productImages,
            'realtedproducts':realtedproducts
         }
        return render(request,self.template_name,context)

   
