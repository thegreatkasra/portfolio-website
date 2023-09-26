from django.shortcuts import render 
from website.forms import ContactForm 
from django.contrib import messages
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request , messages.SUCCESS, 'Successfull !') #success message
            #return JsonResponse({'success': True})
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']

            # Send the email to kasra
            send_mail(
                subject,
                message,
                sender,
                ['kasra.torabiii@gmail.com'],
            )

        else:           
            messages.add_message(request,messages.ERROR, 'ERROR! Try again carefully!') #error message
            #return JsonResponse({'success': False})
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form} )


def full_stack(request):
    return render(request,'cer/full-stack.html')
def python(request):
    return render(request,'cer/python.html')
def mcsa(request):
    return render(request,'cer/mcsa.html')
def mcitp(request):
    return render(request,'cer/mcitp.html')