import json
from django.http import JsonResponse, HttpResponseBadRequest
from email_campaign_manager.services.campaign_services import run_daily_campaign, run_campaign_by_id

def execute_campaign(request):
    if request.method == 'POST':
        try:
            response = run_daily_campaign()
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({'status': 'failure', 'error': str(e)})
    else:
        return HttpResponseBadRequest("Invalid request method")

def execute_campaign_by_id(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        campaign_id = data.get('campaign_id')
        if not campaign_id:
            return JsonResponse({'status': 'failure', 'error': 'Campaign ID is required'})

        try:
            response = run_campaign_by_id(campaign_id)
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({'status': 'failure', 'error': str(e)})
    else:
        return HttpResponseBadRequest("Invalid request method")
