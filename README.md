# Email Campaign Manager

This Django project is an Email Campaign Manager that allows you to manage subscribers, send emails, and run daily campaigns.

## Features
- Add subscribers
- Unsubscribe users via an endpoint
- Mark unsubscribed users as "inactive"
- Use Django Admin to manage records
- Send daily email campaigns with Mailgun using SMTP
- Asynchronous task queue with Celery for optimized email dispatch

## Getting Started

### Prerequisites
- Python
- RabbitMQ
- Mailgun account

### Installation
1. Clone the repository

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Create `.env` file with Mailgun and other configurations:
   ```env
   SMTP_USERNAME=your-mailgun-username
   SMTP_PASSWORD=your-mailgun-password
   SMTP_FROM=your-email-address
   ```

4. Run migrations
   ```bash
   python manage.py migrate
   ```

5. Create a superuser for Django Admin
   ```bash
   python manage.py createsuperuser
   ```

6. Run the server
   ```bash
   python manage.py runserver
   ```

7. Start Celery worker
   ```bash
   celery -A your_project_name worker --loglevel=info
   ```

## Models Schema
### Subscriber
- `email`: EmailField, unique
- `first_name`: TextField
- `is_active`: BooleanField, default=True

### Campaign
- `campaign_id`: UUIDField, unique
- `subject`: TextField
- `preview_text`: TextField
- `article_url`: TextField
- `html_content`: TextField
- `plain_text_content`: TextField
- `published_date`: DateTimeField

## Endpoints
### Admin Interface
- **Admin Dashboard**: Navigate to `/admin/` to access the Django admin dashboard.

### Campaign Operations
- **Execute Daily Campaigns**: 
  - **Method**: POST
  - **URL**: `/email/send/daily/`
  - **Description**: Triggers the sending of daily email campaigns to all active subscribers.

- **Execute Campaign Using campaign_id**:
  - **Method**: POST
  - **URL**: `/email/send/`
  - **Data**: `campaign_id`
  - **Description**: Triggers the sending of email campaign for the specified campaign_id


### Subscriber Operations
- **Add Subscriber**:
  - **Method**: POST
  - **URL**: `/subscriber/add/`
  - **Data**: `email`, `first_name`
  - **Description**: Adds a new subscriber to the mailing list.
  
- **Unsubscribe**:
  - **Method**: POST
  - **URL**: `/subscriber/unsubscribe/`
  - **Data**: `email`
  - **Description**: Unsubscribes a user from the mailing list.
