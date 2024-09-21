from django.shortcuts import render
from .models import Contact
from django.core.mail import send_mail

def home(request):
    return render(request, 'calculator/home.html')

def about(request):
    return render(request, 'calculator/about.html')

def projects(request):
    return render(request, 'calculator/projects.html')

def blog(request):
    return render(request, 'calculator/blog.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # Save the contact message to the database
        contact = Contact(name=name, email=email, message=message)
        contact.save()

        # Send a confirmation email to the user
        send_mail(
            'Message Received',  # Subject
            f'Thank you {name}, your message has been successfully sent!',  # Message content
            'Negative Zero <negativezero48@gmail.com>',  # From email with name
            [email],  # To email
            fail_silently=False,
        )

        # Render the contact page with a success message
        return render(request, 'calculator/contact.html', {'success': True})
    
    return render(request, 'calculator/contact.html')