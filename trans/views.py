from django.shortcuts import render
import googletrans
# Create your views here.
def index(request):
    bf = request.GET.get("bf", "")
    fr = request.GET.get("fr", "")
    to = request.GET.get("to", "")
    context = {
        "ndict" : googletrans.LANGUAGES
    }
    if bf:
        tra = googletrans.Translator()
        af = tra.translate(bf, src=fr, dest=to)
        context.update({
            "af": af.text,
            "bf": bf,
            "fr": fr,
            "to": to,
        })
    return render(request, "trans/index.html", context)