# analyser/views.py
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .utils import MailAnalyserDummy
from django.views.decorators.csrf import csrf_exempt
import os
API_TOKEN = "SecretToken123"
# Instance of the model
analyser = MailAnalyserDummy()
print(analyser.getEmotions("HOLA"))

def index(request):
    # frontend with js
    return render(request, "analyser/index.html")
# Token 


@csrf_exempt 
@require_POST
def analyse_mail_api(request):
    # Check token 
    token = request.headers.get("Authorization")
    if token != f"Token {API_TOKEN}":
        return JsonResponse({"error": "Unauthorized"}, status=401)

    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    mail = payload.get("mail", "").strip()
    if not mail:
        return JsonResponse({"error": "No mail content provided"}, status=400)

    # analyze mail
    emotions = analyser.getEmotions(mail)
    topics = analyser.getTopics(mail)

    # scores to float to valid json
    emotions = {k: float(v) for k, v in emotions.items()}
    print(emotions)

    return JsonResponse({"emotions": emotions, "topics": topics})