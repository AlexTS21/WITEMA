from django.shortcuts import render
from .utils import MailAnalyser

# Instanciamos la clase una sola vez
analyser = MailAnalyser()

def analyse_mail(request):
    """
    Vista que maneja el formulario con textarea para analizar mails
    """
    emotions = None
    topics = None

    if request.method == "POST":
        mail = request.POST.get("mail", "")
        if mail:
            emotions = analyser.getEmotions(mail)
            topics = analyser.getTopics(mail)

    return render(request, "analyser/index.html", {  # Asegúrate que el path coincide con la carpeta de templates
        "emotions": emotions,
        "topics": topics
    })
