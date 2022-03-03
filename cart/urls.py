from django.urls import path
from . import views 
 

urlpatterns = [ 
    path('add-to-cart',views.AddToCart.as_view(),name="AddToCart"),
    path('my-cart',views.MyCart.as_view(),name="MyCart"),
    path('checkout',views.CheckOut.as_view(),name="CheckOut"),
    path('payment-successs',views.Payment_Success.as_view(),name="PaymentSuccesss"),
    # path('capture-payment/',views.CapturePayment.as_view(),name="Capturepayment"),
    path('webhook',views.RazorpayWebhook),
    path('thank-you',views.ThankYou,name="ThankYou"),
 ]