import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exercise_log.settings')

app = Celery('exercise_log')
app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULTS_BACKEND=os.environ['REDIS_URL'])
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'create-or-update-weekly-summary': {
#         'task': 'api.create_or_update_weekly_summary',
#         'schedule': timedelta(weeks=1),
#         'args': (),  # '0 0 * * 1'
#     }
# }
