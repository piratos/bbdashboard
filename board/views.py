from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

import datetime

# REST client
from dash.BaseClient import BuildsClient, BuildersClient

# Create your views here.
class indexView(View):
	def get(self, request):
		buildsclient = BuildsClient()
		buildersclient = BuildersClient()
		builders = buildersclient.list()
		builders = {i['builderid']:0 for i in builders}
		builds = buildsclient.list()
		failed_builds = 0
		for build in builds:
			if build['state_string'] != 'build successful':
				builders[build['builderid']] += 1
				failed_builds += 1
			build['complete_at'] = datetime.datetime.fromtimestamp(
				int(build['complete_at']))
		# convert failed builds by builder to list of %.
		builders = [round((100*float(i))/failed_builds, 2) for i in builders.values()]
		failed_builds = round((100*float(failed_builds))/len(builds), 2)
		return render(request, 'index.html', {'builds': builds,
			                                  'failed': failed_builds,
			                                  'builders': builders})