from django.shortcuts import render, redirect
# Create your views here.
from django.views import View
from cart.models import Cart
from product.models import ProductCategory ,Product

class AddToCart(View):

    def post(self,request):
        print(request.POST)
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        cart,created = Cart.objects.get_or_create(product_id=product_id,user_id=request.user.id)
        if created:
            cart.quantity = quantity
        else:
            cart.quantity= int(quantity)+ int(cart.quantity) 
        cart.save()
        '''TRADITIONAL WAY TO UPDATE DATA IN DB'''
        # try:
        #     cart = Cart.objects.get(product_id=product_id,user_id=request.user.id)
        #     cart.quantity= int(quantity)+ int(cart.quantity)
        #     cart.save()

        # except Cart.DoesNotExist:
            
        #     Cart.objects.create(
        #         quantity = quantity,
        #         product_id= product_id,
        #         user  = request.user
        #     )

        return redirect("ProductDetails",product_id=product_id)


class MyCart(View):
    
    template_name="my-cart.html"
   
    def get(self,request):
        navigationProductCategory = ProductCategory.objects.filter(status=True)
        carts = Cart.objects.filter(user=request.user)
        
        cartData={}
        subtotal = 0
        shippingCost = 50
        total = 0 
        for key,cart in enumerate(carts):
            productTotal = int(cart.product.price)* int(cart.quantity)
            subtotal +=  productTotal
            
            cartData[key]={
                'product_image':cart.product.cover_img,
                'product_name':cart.product.name,
                'product_price':cart.product.price,
                'quantity':cart.quantity,
                "product_total":productTotal,
                "cart_id":cart.id
            }
        
        total = subtotal + shippingCost

        context = {
            "navigationProductCategory":navigationProductCategory,
            "carts":list(cartData.values()),
            "subtotal":subtotal,
            "shippingCost":shippingCost,
            "total":total
         }
        return render(request,self.template_name,context)


    def post(self,request):
        cart_id_list= request.POST.getlist('cart_id')
        quantity_list = request.POST.getlist('quantity')
          
        for index,cart_id in enumerate(cart_id_list):
            # print(index,cart_id,quantity_list[index])
            try:
                cartObject = Cart.objects.get(id= cart_id)
                if int(quantity_list[index]) == 0:
                    cartObject.delete()
                else:      
                    cartObject.quantity = quantity_list[index]
                    cartObject.save()

            except Cart.DoesNotExist:
                pass
        return redirect("MyCart")

class CheckOut(View):
    template_name="checkout.html"

    def get(self,request):
        navigationProductCategory = ProductCategory.objects.filter(status=True)
        carts = Cart.objects.filter(user=request.user)
        cartData={}
        subtotal = 0
        shippingCost = 50
        total = 0 
        for key,cart in enumerate(carts):
            productTotal = int(cart.product.price)* int(cart.quantity)
            subtotal +=  productTotal
            
            cartData[key]={
                'product_name':cart.product.name,
                "product_total":productTotal
            }
        
        total = subtotal + shippingCost

        context = {
            "navigationProductCategory":navigationProductCategory,
            'carts':list(cartData.values()),
            'subtotal':subtotal,
            'shippingCost':shippingCost,
            'total':total
         }
        return render(request,self.template_name,context)