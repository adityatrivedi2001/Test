from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import contactus
from django.core.mail import send_mail

# Create your views here.
def homepage(request):
	return render(request = request,
				  template_name = 'index.html',
				  context = {'context':contactus.objects.all})

def ctus(request):
	if request.method == 'POST':
		name1 = request.POST['ctus_name']
		email1 = request.POST['ctus_email']
		message12 = request.POST['ctus_message']
		cont_obj = contactus(name = name1,email = email1,message1 = message12)
		cont_obj.save()
		send_mail(
	    'Name :- ' + name1 + ' Email :- ' + email1,
	    message12,
	    'KhalidJain3@gmail.com',
	    ['amolpandey33@gmail.com'],
	    fail_silently=False,
	    )
		print('again ok')
		return redirect('/')
	else:
		print('ok')
		return redirect('/')

def even(request):
	return render(request, 'eventenq.html')
