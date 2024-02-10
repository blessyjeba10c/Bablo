from django.http import HttpResponse, render_template, request,jsonify,session
from django.shortcuts import render__template
from django.views.decorators.csrf import csrf_exempt
from .message_completion import Message_Completion, Test
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

urlpatterns = [
    path('mentor/chat/<str:assistant_model>', MessageCompletion.as_view(), name='message_completion'),
    path('test/', Test.as_view(), name='test'),
]

