from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Challenge
from .bl.GuessChecker import GuessChecker as GC

# Create your views here.
def index(request):
    is_correct = None
    challenge = Challenge.objects.first()

    if request.method == "POST":
        guess = request.POST.get("guess", "")
        is_correct = GC.checkGuess(guess)

    context = {
        "challenge": challenge,
        "is_correct": is_correct
    }

    return render(request, "index.html", context)


def challenge_list(request):
    all_challenges = Challenge.objects.all()
    context = {
        "challenges": all_challenges
    }
    return render(request, "index.html", context)

