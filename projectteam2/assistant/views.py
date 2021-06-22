from django.http import HttpResponse
from django.shortcuts import render
from .models import Documents
from .models import *
from datetime import date
from django.core.mail import send_mail


def home(request):
    return render(request, 'CarAssistant/homepage.html')


def sign_up(request):
    return render(request, 'CarAssistant/signup.html')


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
    # render(request, "document/detail.html", {})

def get_documents_to_expire(request):
    number_of_emails_sent = 0
    all_documents = Documents.objects.all()

    for doc in all_documents:
        time_to_expire = (doc.expiry_date - date.today()).days
        if time_to_expire < 30:
            number_of_emails_sent = number_of_emails_sent + 1

            corresponding_car = Car.objects.get(pk=doc.car.id)
            corresponding_user = User.objects.get(pk=corresponding_car.user.id)
            send_mail(
                str(doc.name) + ' is about to expire',
                'We just want to let you know that your '
                + str(doc.name) + ' will expire soon('
                + str(time_to_expire) + ' days) for '
                + str(corresponding_car.model) + ' '
                + str(corresponding_car.type)
                + '. Please consider renewing it.',
                'assistant@mycar.com',
                [corresponding_user.email],
                fail_silently=False,
            )

    return HttpResponse(str(number_of_emails_sent) + " email(s) were sent")


#def get_cars(request):
#    all_cars = Car.objects.all()
 #   context = {'list of cars': all_cars}
  #  return render(request, 'CarAssistant/cars.html', context)
