from django.http import HttpResponse
from django.shortcuts import render
from .models import Documents

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index2(request):
    return HttpResponse("HTESTTT.")

def get_documents_to_expire(request):
    obj = Documents.objects.get(id=1)
#    context = {
 #       'doc_name': obj.name,
  #      'doc_expiry_date': obj.expiry_date
   # }
    return HttpResponse(obj.name)
        #render(request, "document/detail.html", {})


def home(request):
    return render(request, 'CarAssistant/homepage.html')


def sign_up(request):
    return render(request, 'CarAssistant/signup.html')


