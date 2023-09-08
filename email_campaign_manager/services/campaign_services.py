import datetime
from email_campaign_manager.models.campaign_model import Campaign
from email_campaign_manager.models.subscriber_model import Subscriber
from email_campaign_manager.services.email_services import send_email
from django.template.loader import render_to_string

def run_daily_campaign():
    # Get today's campaigns
    today = datetime.date.today()
    campaigns = Campaign.objects.filter(published_date__date=today)

    # Get active subscribers
    active_subscribers = Subscriber.objects.filter(is_active=True)
    email_list = [subscriber.email for subscriber in active_subscribers]
    
    for campaign in campaigns:
        # Load email template and populate it with campaign info
        html_content = render_to_string('email_template.html', {
            'subject': campaign.subject,
            'preview_text': campaign.preview_text,
            'article_url': campaign.article_url,
            'html_content': campaign.html_content,
        })
        
        # Send the email
        send_email(email_list, campaign.subject, html_content)

    return {"status_code": 200, "message": "Email sent to all users for all campaigns today"}