from django.http import JsonResponse
from email_campaign_manager.services.campaign_services import run_daily_campaign

def execute_campaign(request):
    try:
        response = run_daily_campaign()
        return JsonResponse(response)
    except Exception as e:
        return JsonResponse({'status': 'failure', 'error': str(e)})
