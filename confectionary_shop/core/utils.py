import random

import redis
from kavenegar import *
import pytz
from django.utils import timezone
import jdatetime


def convert_time_to_jalali(date_time):
    date_time = str(date_time).split(' ')
    part_1 = date_time[0].split('/')
    d_time = jdatetime.date.fromgregorian(year=int(part_1[2]), month=int(part_1[1]), day=int(part_1[0]))
    return d_time


def convert_to_localtime(utctime):
    fmt = '%d/%m/%Y %H:%M'
    local_dt = timezone.localtime(utctime, pytz.timezone('Asia/Tehran'))
    return convert_time_to_jalali(local_dt.strftime(fmt))


def send_otp(phone):
    r = redis.Redis()
    code = random.randint(1000, 9999)
    print(code)
    r.set(name=phone, value=code, ex=60)
    try:
        import json
    except ImportError:
        import simplejson as json
    try:
        api = KavenegarAPI('6B614F7A4E7873373678575A6D7633314B4E5A763074714F574A7A503779685253323761494A792B7648593D')
        params = {
            'sender': '0018018949161',  # optional
            'receptor': phone,  # multiple mobile number, split by comma
            'message': f'your code : {code}',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


def check_otp(phone, code):
    r = redis.Redis()
    print(phone)
    _ = r.get(phone)
    print(_)
    if _ and str(_.decode('utf8')) == str(code):
        return True
    return False
