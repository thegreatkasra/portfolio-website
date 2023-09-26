from django.shortcuts import render 
from website.forms import ContactForm 
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from website.models import Post
from django.shortcuts import render ,get_object_or_404

def index(request):
    current_time = timezone.now()
    posts = Post.objects.filter(published_date__lte=current_time, status=1).order_by('-published_date')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request , messages.SUCCESS, 'Successfull !') #success message
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

    else:
        form = ContactForm()
    context = {'posts': posts , 'form': form}
    return render(request, 'index.html', context)

def single(request, pid):
    current_time = timezone.now() 
    all_posts = Post.objects.all()
    post = get_object_or_404(all_posts, pk=pid, status=1 ,published_date__lte=current_time)
    context = {
           'post': post,
       }
    return render(request,'index.html',context)



def full_stack(request):
    return render(request,'cer/full-stack.html')
def python(request):
    return render(request,'cer/python.html')
def mcsa(request):
    return render(request,'cer/mcsa.html')
def mcitp(request):
    return render(request,'cer/mcitp.html')