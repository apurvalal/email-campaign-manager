"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from email_campaign_manager.controllers.campaign_controller import execute_campaign, execute_campaign_by_id
from email_campaign_manager.controllers.subscriber_controller import add_subscriber, unsubscribe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('email/send/daily/', execute_campaign),
    path('email/send/', execute_campaign_by_id),
    path('subscriber/add/', add_subscriber),
    path('subscriber/unsubscribe/', unsubscribe)
]
