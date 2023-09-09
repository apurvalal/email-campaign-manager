from django.contrib import admin
from email_campaign_manager.models.campaign_model import Campaign

class CampaignAdmin(admin.ModelAdmin):
    list_display = ('subject', 'campaign_id', 'published_date')

admin.site.register(Campaign, CampaignAdmin)
