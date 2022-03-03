from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from cart.models import Cart, Couponcode
from product.models import ProductCategory ,Product
from order.models import Order, OrderDetail , Payment

import datetime
import razorpay
import json 


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

        # couponcode = Couponcode.objects.get()
        # coupon = request.POST.get('coupon')
        # print("AAHAAAA",coupon)
        # if coupon == 'disc50':
        #     print("***APPLIED ***",couponcode.amount)

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

        couponcode = Couponcode.objects.get()
        coupon = request.GET.get('coupon')       
 
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
        if coupon == 'disc50':
            total = subtotal + shippingCost - couponcode.amount
            context = {
                "navigationProductCategory":navigationProductCategory,
                'carts':list(cartData.values()),
                'subtotal':subtotal,
                'shippingCost':shippingCost,
                'couponcode':couponcode.amount,
                'total':total
            }
        else:
            total = subtotal + shippingCost

            context = {
                "navigationProductCategory":navigationProductCategory,
                'carts':list(cartData.values()),
                'subtotal':subtotal,
                'shippingCost':shippingCost,
                'couponcode':"0",
                'total':total
            }
        return render(request,self.template_name,context)

    def post(self,request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        carts = Cart.objects.filter(user=request.user)
        cartData={}
        subtotal = 0
        shippingCost = 50
        total = 0 
        for key,cart in enumerate(carts):
            productTotal = int(cart.product.price)* int(cart.quantity) 
            subtotal +=  productTotal
      
        total = (subtotal + shippingCost)* 100
      
      
        client = razorpay.Client(auth=("rzp_test_jRr4U6mfmGQsBc", "NWTh9qgQKzOkjCRbTpDV67BJ"))
        receipt = f'order_rcptid{request.user.id}'
        data = { "amount": total, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data)
        print(payment)
        if payment.get('id'):
            context = { 
                "order_id": payment['id'],
                'amount': payment['amount'],
                'first_name':first_name,
                'last_name':last_name,
                'address':address,
            }
            return render(request,'capture-payment.html',context)
 


class Payment_Success(View):
    def post(self, request):
        razorpay_payment_id= request.POST.get('razorpay_payment_id')
        razorpay_order_id= request.POST.get('razorpay_order_id')
        razorpay_signature= request.POST.get('razorpay_signature')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        address= request.POST.get('address')
        carts = Cart.objects.filter(user=request.user)
        if carts:
            order = Order.objects.create( 
                user = request.user,
                name = f'{first_name} {last_name}',
                address = address,
                razorpay_order_id = razorpay_order_id
            )
            for cartss in carts:
                OrderDetail.objects.create(
                order = order,
                product = cartss.product,
                price = cartss.product.price,
                quantity = cartss.quantity
                )       
                carts.delete()         
        return JsonResponse({'status': 'success'})



@csrf_exempt
def RazorpayWebhook(request):
    print(request.body)
    requestBody = json.loads(request.body.decode('utf-8'))
    payload = requestBody['payload']
    if payload['payment']:
        order_id = payload['payment']['entity']['order_id']
        try:
            order = Order.objects.get(razorpay_order_id= order_id)
            payment = Payment.objects.get_or_create(order = order)
            payment.payment_id =  payload['payment']['entity']['order_id'],
            payment.payment_status = payload['payment']['entity']['status'],
            payment.payment_method =  payload['payment']['entity']['method'],
            payment.created_at = payload['payment']['entity']['created_at'],
            payment.amount = payload['payment']['entity']['amount'],
            payment.save()
            order.payment_status = True
            order.save()
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'failed'})

    return JsonResponse({'status': 'success'})


def ThankYou(request):
    return HttpResponse("<h1>Your order has been successfully placed</h1>")

