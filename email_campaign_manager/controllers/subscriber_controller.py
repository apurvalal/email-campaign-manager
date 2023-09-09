from django.http import JsonResponse, HttpResponseBadRequest
from email_campaign_manager.models.subscriber_model import Subscriber
import json

def add_subscriber(request):
    """
    Add a new subscriber to the email list. 
    """

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        email = data.get('email')
        first_name = data.get('first_name')
        
        # Check if email is already in the database
        if Subscriber.objects.filter(email=email).exists():
            return JsonResponse({"status_code": 400, "message": "Subscriber already exists"})
        
        try:
            Subscriber.objects.create(email=email, first_name=first_name, is_active=True)
        except Exception as e:
            return JsonResponse({"status_code": 500, "message": f"An error occurred: {str(e)}"})
        
        return JsonResponse({"status_code": 200, "message": "Subscriber successfully created"})
    else:
        return HttpResponseBadRequest("Invalid request method")

def unsubscribe(request):
    """
    Unsubscribe an existing subscriber from the email list.
    """
    
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        
        try:
            subscriber = Subscriber.objects.get(email=email)
            subscriber.is_active = False
            subscriber.save()

        # Check if subscriber exists
        except Subscriber.DoesNotExist:
            return JsonResponse({"status_code": 404, "message": "Subscriber not found"})
        
        except Exception as e:
            return JsonResponse({"status_code": 500, "message": f"An error occurred: {str(e)}"})
        
        return JsonResponse({"status_code": 200, "message": "Unsubscribed successfully"})
    else:
        return HttpResponseBadRequest("Invalid request method")
