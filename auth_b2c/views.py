from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth import logout
from auth_b2c.models import *
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            if request.POST['password1'] == request.POST['password2']:    
                form.save()
                messages.success(request, 'Cuenta creada exitosamente')
                correo = request.POST['email']
                nombre = request.POST['first_name']
                mail = create_mail(
                    correo,
                    'Felicidades, ya estas registrado en B2C Store',
                    'correos/registro.html',
                    {
                        'user': nombre
                    }
                    )
                mail.send(fail_silently=False)
                return redirect('login')
            else:
                messages.error(request, 'Las contraseñas no coinciden')
                return render(request, 'register.html', {'title': 'Registro'})
        else:
            messages.error(request, 'Algun campo no cumple con los requisitos')
            return redirect('register')
    else:
        form = RegistroForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def exit(request):
    logout(request)
    return redirect('/')

def create_mail(user_mail, subject, template_name, context):
    template = get_template(template_name)
    content = template.render(context)

    message = EmailMultiAlternatives(
        subject=subject,
        body='',
        from_email=settings.EMAIL_HOST_USER,
        to=[
            user_mail
        ],
        cc=[]
    )

    message.attach_alternative(content, 'text/html')
    return message