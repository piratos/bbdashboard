from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# REST client
from dash.BaseClient import BuildsClient

# Create your views here.
class indexView(View):
	def get(self, request):
		buildsclient = BuildsClient()
		builds = buildsclient.list()
		return render(request, 'index.html', {'builds': builds})