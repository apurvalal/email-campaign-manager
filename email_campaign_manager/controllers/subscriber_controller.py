from django.http import JsonResponse
from email_campaign_manager.models.subscriber_model import Subscriber

def add_subscriber(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        Subscriber.objects.create(email=email, first_name=first_name, is_active=True)
        return JsonResponse({"status_code": 200, "message": "Subscriber successfully created"})

def unsubscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subscriber = Subscriber.objects.get(email=email)
        subscriber.is_active = False
        subscriber.save()
        return JsonResponse({"status_code": 200, "message": "Unsubscribed successfully"})
