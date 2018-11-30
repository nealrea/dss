from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic

from django.http import HttpResponse

from documents.models import Document
from documents.models import CustomUser

def Profile(request):	
	if request.user.is_authenticated:
		my_id = str(request.user.id)
		user = CustomUser.objects.filter(id=request.user.id)
		for u in user:
			interests = u.interests
		allDocs = Document.objects.all()
		sharedDocs = []
		publicDocs = []
		for doc in allDocs:
			collaborators = doc.collaborators.split('/')
			if my_id in collaborators:
				sharedDocs.append(doc)
			if doc.private == False:
				publicDocs.append(doc)
		return render(request, 'profile.html', {
	    	'myDocs': Document.objects.filter(owner=request.user.id),
	    	'sharedDocs': sharedDocs,
	    	'publicDocs': publicDocs,
	    	'interests': interests,
	    })
	else:
		my_id = str(request.user.id)
		allDocs = Document.objects.all()
		sharedDocs = []
		publicDocs = []
		for doc in allDocs:
			collaborators = doc.collaborators.split('/')
			if my_id in collaborators:
				sharedDocs.append(doc)
			if doc.private == False:
				publicDocs.append(doc)
		return render(request, 'profile.html', {
	    	'myDocs': Document.objects.filter(owner=request.user.id),
	    	'sharedDocs': sharedDocs,
	    	'publicDocs': publicDocs,
	    })

def Home(request):
	return render(request, 'home.html')