from django.shortcuts import render, redirect
from sparkpost import SparkPost
from datetime import datetime, time
from django.http import HttpResponse
from . models import ScheduledMail

def index(request):

    sm = ScheduledMail.objects.all()[:100]

    context = {'sm' : sm}
    return render(request, 'index.html', context)

def details(request,id):
    sm = ScheduledMail.objects.get(id=id)

    context = {'sm': sm}
    return render(request, 'details.html', context)

def compose(request):
    now = datetime.now()

    if(request.method== "POST"):
        recipient = request.POST['recipient']
        sender = request.POST['sender']
        subject = request.POST['subject']
        message = request.POST['message']
        setDelivery = request.POST['setDelivery']

        sm = ScheduledMail(recipient = recipient, sender = sender,
                           subject = subject, message = message, setDelivery = setDelivery)
        sm.save()

        while():
            now = datetime.now()
            if(now == setDelivery):
                break;

        sp = SparkPost('')

        response = sp.transmissions.send(
            recipients=[recipient],
            html=message,
            from_email=sender,
            subject=subject
        )

        print(response)



        return redirect('/ScheduledMail')

    else:
        return render(request, 'compose.html')