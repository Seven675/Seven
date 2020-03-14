
from datetime import datetime, timedelta
import os
import sys
from os.path import dirname, abspath

import django

path = dirname((abspath(dirname(__file__))))
sys.path.insert(0, path)
# env = os.getenv('DJANGO_ENV', 'development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PCCR.settings')
django.setup()


def set_booking_status_to_zero():
    from individual.models import Wxuser
    thirty_before = datetime.now() - timedelta(minutes=30)
    wxuser = Wxuser.objects.filter(order_status=0, ava__booking_status='1', ava__update_time__lt=thirty_before)
    if wxuser.count() > 0:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), wxuser.count())
    for user in wxuser:
        user.ava.booking_status = '0'
        user.ava.save()

