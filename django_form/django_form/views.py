from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django_form.form import ContactForm

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			'''
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@example.com'),
				['siteowner@example.com'],
			)
			'''
			print(cd)
			return HttpResponseRedirect('/contact')

	else:
		form = ContactForm()
	return render_to_response('contact_form.html', {'form': form})





