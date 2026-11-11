from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Challenge

# Create your views here.
def index(request):
	template = loader.get_template("index.html")
	return HttpResponse(template.render())

def challenge_list(request):
	all_challenges = Challenge.objects.all()
	context = {
		"challenges": all_challenges
	}
	
	return render(request, "index.html", context)

