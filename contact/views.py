from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.core.mail import BadHeaderError, message, send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from contact.models import ContectUs
# Create your views here.
class ContactView(View):
    def get(self,request):
        gretting = {"title":"Contact"}
        return render(request,"dashboard/contact.html",gretting)
    def post(self,request):
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            comment = request.POST.get("comments")
            # if name and email and subject and comment != "":
            #     subject1 = "Thank You"
            #     subject = "Contect Us"
            #     from_mail = 'sozia@support.com'
            #     message = "Thank you for contact us"
            #     send_mail(subject1, message, from_mail, [email],fail_silently=False)
            #     contact = ContectUs.objects.create(name=name,email=email,subject=subject,comment=comment)
            # data = {
            #     'success_message' : 'Email Successfully send'
            # }
            # return JsonResponse(data,safe=False)
            return redirect('/contact')
        
        
        
        