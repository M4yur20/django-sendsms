from django.shortcuts import render, HttpResponse
from .models import Score
from twilio.rest import Client


def sendsms_view(request):
    if request.method == 'POST':
        number_i = int(request.POST.get('number'))
        number = request.POST.get('number')
        score = request.POST.get('score')
        score_i = int(request.POST.get('score'))
        instance = Score(result=score_i,number=number)
        instance.save()
        if score_i < 70:
            account_sid = 'ACfe2bd2213e80e24fedef2491644e87f3'
            auth_token = '4567137140be96fc788a88c41f41d2dd'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=f'The current result is bad - {score}',
                from_='+12108801629',
                to=f'+91{number_i}'
            )
            print(message.sid)
            return render(request, 'main.html')
        else:
            account_sid = 'ACfe2bd2213e80e24fedef2491644e87f3'
            auth_token = '4567137140be96fc788a88c41f41d2dd'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=f'The current result is very good - {score}',
                from_='+12108801629',
                to=f'+91{number_i}')
            print(message.sid)
            return HttpResponse('Sms Sent Successfully')
    return render(request,'main.html')


def success_view(request):
    return HttpResponse("Sent Sms Successfully")
