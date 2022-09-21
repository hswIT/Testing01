from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
import logging
from shop.models import Product

class DashboardView(View):
    def get(self,request):
        gretting = {"title":"Home"}
        return render(request,"dashboard/index.html",gretting)
class AboutView(View):
    def get(self,request):
        gretting = {"title":"About"}
        return render(request,"dashboard/about.html",gretting)
    

def search(request):
        queryset_list = Product.objects.order_by('-list_date')
        
        if 'keywords' in request.GET:
            keywords = request.GET['keywords']
            if keywords == "":
                queryset_list = None       
            else:
               queryset_list = queryset_list.filter(description__icontains=keywords)
                  
        else:
            queryset_list = None
              
        context = {
            'products':queryset_list,
        }
               
        return render(request,'dashboard/search.html',context)
    

    
    
