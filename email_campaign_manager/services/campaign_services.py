import datetime
from email_campaign_manager.models.campaign_model import Campaign
from email_campaign_manager.models.subscriber_model import Subscriber
from email_campaign_manager.services.email_services import send_email, send_bulk_emails
from django.template.loader import render_to_string
import logging

logger = logging.getLogger('django')

def run_daily_campaign():
    try:
        # Get today's campaigns
        today = datetime.date.today()
        campaigns = Campaign.objects.filter(published_date__date=today)

        logger.info(f"Campaigns for today {campaigns}")

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
            send_bulk_emails(email_list, campaign.subject, html_content)

        return {"status_code": 200, "message": "Email sent to all users for all campaigns today"}
    except Exception as e:
        logger.error(f"An error occurred while running the daily campaign: {str(e)}")
        return {"status_code": 500, "message": f"An error occurred: {str(e)}"}

def run_campaign_by_id(campaign_id):
    try:
        campaign = Campaign.objects.get(id=campaign_id)
        
        # Get active subscribers
        active_subscribers = Subscriber.objects.filter(is_active=True)
        email_list = [subscriber.email for subscriber in active_subscribers]
        
        # Load email template and populate it with campaign info
        html_content = render_to_string('email_template.html', {
            'subject': campaign.subject,
            'preview_text': campaign.preview_text,
            'article_url': campaign.article_url,
            'html_content': campaign.html_content,
        })
        
        # Send the email
        send_bulk_emails(email_list, campaign.subject, html_content)
        
        return {"status_code": 200, "message": f"Email sent to all users for campaign {campaign_id}"}
    except Campaign.DoesNotExist:
        logger.error(f"Campaign with ID {campaign_id} not found")
        return {"status_code": 404, "message": "Campaign not found"}
    except Exception as e:
        logger.error(f"An error occurred while running the campaign: {str(e)}")
        return {"status_code": 500, "message": f"An error occurred: {str(e)}"}
