from django.shortcuts import redirect, render
from django.views import View
from dashboard.forms import dashboardForm

# Create your views here.
# def dashboard(request):
#     dashboardForms = dashboardForm.objects.all( ).first()
#     form_class = dashboardForm(request.POST or None,instance=dashboardForms)
#     if form_class.is_valid():
#         form_class.save()
#     context ={
#         'forms':form_class
#     }
#     return render(request,"dashboard.html",context)


class dashboard(View):
    form_class = dashboardForm
    def get(self,request):
        form_class = self.form_class()
        context = {
            'form':form_class
        }
        return render(request,"dashboard.html",context)
    
    def post(self,request):
        form_class = self.form_class(request.POST)
        if form_class.is_valid():
            form_class.save()
            return redirect('dashboard')
        else:
            context = {
            'form':form_class
            }
        return render(request,"dashboard.html",context) 