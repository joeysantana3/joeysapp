from django.shortcuts import render
from django.http import HttpResponse
import os
import logging

logging.basicConfig(filename='/home/ubuntu/debug.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


def hello_world(request):
    instance_id = os.environ.get('INSTANCE_ID')
    print(instance_id)
    logging.debug('Running hello_world')
    logging.debug(f"Instance id set to {instance_id}")
    return HttpResponse(f"Hello, World! I'm {instance_id}")
