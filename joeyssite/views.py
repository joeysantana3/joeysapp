from django.shortcuts import render
from django.http import HttpResponse
import os

def hello_world(request):
    instance_id = os.environ.get('INSTANCE_ID')
    print(instance_id)
    return HttpResponse(f"Hello, World! I'm {instance_id}")
