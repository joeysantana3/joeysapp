from django.shortcuts import render
from django.http import HttpResponse
import os
import logging

logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)

# testing functionality
login_name = os.getlogin()
logging.debug("login name is " + login_name)

def hello_world(request):
    instance_id = os.environ.get('INSTANCE_ID')
    print(instance_id)
    logging.debug('Running hello_world')
    logging.debug(f"Instance id set to {instance_id}")
    return HttpResponse(f"Hello, World! I'm {instance_id}")
