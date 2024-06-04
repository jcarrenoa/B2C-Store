from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse

from store.models import *
from store.forms import PerfilForm

from auth_b2c.models import Perfil

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from datetime import date

import os

# Create your views here.
def index(request):
    proveedor = Proveedor.objects.all()
    if request.user.is_authenticated:
        cantidad_carrito = DetallesCarrito.objects.filter(idCarrito__idPerfil=request.user).count()
        return render(request, 'index.html', {'title': 'Inicio', 'proveedores': proveedor, 'cantidad_carrito': cantidad_carrito})
    else:
        return render(request, 'index.html', {'title': 'Inicio', 'proveedores': proveedor})

def exit(request):
    logout(request)
    return redirect('index')

def tienda(request):
    productos = Producto.objects.filter().all()
    categorias = Categoria.objects.values()
    if request.user.is_authenticated:
        cantidad_carrito = DetallesCarrito.objects.filter(idCarrito__idPerfil=request.user).count()
        return render(request, 'tienda.html', {'productos': productos, 'isnull': Producto.objects.filter().all().count() == 0, 'categorias': categorias, 'title': 'Tienda', 'cantidad_carrito': cantidad_carrito})
    else:
        return render(request, 'tienda.html', {'productos': productos, 'isnull': Producto.objects.filter().all().count() == 0, 'categorias': categorias, 'title': 'Tienda'})
    
def descuento(request):
    descuentos = Descuento.objects.all()
    if request.user.is_authenticated:
        cantidad_carrito = DetallesCarrito.objects.filter(idCarrito__idPerfil=request.user).count()
        return render(request, 'descuentos.html', {'title': 'Descuentos', 'descuentos': descuentos, 'cantidad_carrito': cantidad_carrito})
    else:
        return render(request, 'descuentos.html', {'title': 'Descuentos', 'descuentos': descuentos})
    
def evento(request):
    eventos = Evento.objects.all()
    if request.user.is_authenticated:
        cantidad_carrito = DetallesCarrito.objects.filter(idCarrito__idPerfil=request.user).count()
        return render(request, 'eventos.html', {'title': 'Eventos', 'eventos': eventos, 'cantidad_carrito': cantidad_carrito})
    else:
        return render(request, 'eventos.html', {'title': 'Eventos', 'eventos': eventos})
    
def contacto(request):
    if request.user.is_authenticated:
        cantidad_carrito = DetallesCarrito.objects.filter(idCarrito__idPerfil=request.user).count()
        return render(request, 'contacto.html', {'title': 'Contacto', 'cantidad_carrito': cantidad_carrito})
    else:
        return render(request, 'contacto.html', {'title': 'Contacto'})
    
def search_results(request):
    categorias = Categoria.objects.values()
    query = request.GET.get('query')
    if query:
        productos = Producto.objects.filter(Nombre__icontains=query)
    else:
        productos = Producto.objects.none()
    if request.user.is_authenticated:
        cantidad_carrito = DetallesCarrito.objects.filter(idCarrito__idPerfil=request.user).count()
        return render(request, 'tienda.html', {'productos': productos, 'isnull': Producto.objects.filter().all().count() == 0, 'categorias': categorias, 'title': 'Tienda', 'cantidad_carrito': cantidad_carrito})
    else:
        return render(request, 'tienda.html', {'productos': productos, 'isnull': Producto.objects.filter().all().count() == 0, 'categorias': categorias, 'title': 'Tienda'})
    
def contacto(request):
    if request.method == 'POST':
        options = {'1': 'Soporte', '2': 'Ventas', '3': 'Otros'}
        motivo = options[request.POST.get('motivo')]
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        mensaje = request.POST.get('mensaje')
        telefono = request.POST.get('telefono')
        string = f'Mensaje de contacto de {nombre} ({correo}) con motivo {motivo}'
        template = render_to_string('correos/contacto_template.html', {
            'nombre': nombre, 'correo': correo, 'mensaje': mensaje, 'motivo': motivo, 'telefono': telefono
            })
        email = EmailMessage(
            string,
            template,
            settings.EMAIL_HOST_USER,
            ['b2c.contact.mvp@gmail.com'],
            )
        email.fail_silently = False
        email.send()
        mail = create_mail(
            correo,
            'Gracias por contactarnos',
            'correos/agradecimientos.html',
            {
                'user': nombre
            }
            )

        mail.send(fail_silently=False)
        messages.success(request, 'Mensaje enviado correctamente')
    if request.user.is_authenticated:
        cantidad_carrito = DetallesCarrito.objects.filter(idCarrito__idPerfil=request.user).count()
        return render(request, 'contacto.html', {'title': 'Contacto', 'cantidad_carrito': cantidad_carrito})
    else:
        return render(request, 'contacto.html', {'title': 'Contacto'})

@login_required
def configuracion(request):
    user = Perfil.objects.get(pk=request.user.id)
    cantidad_carrito = DetallesCarrito.objects.filter(idCarrito__idPerfil=request.user).count()
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=user)
        #if form.is_valid():
        if request.FILES.get('imagen') != None or request.FILES.get('portada') != None or request.POST.get('nacimiento') != None:
            if request.FILES.get('imagen'):
                user.imagen = request.FILES.get('imagen')
            if request.FILES.get('portada'):
                user.portada = request.FILES.get('portada')
            if request.POST.get('nacimiento') != "":
                user.nacimiento = request.POST.get('nacimiento')
            user.save()
            messages.success(request, 'Cambios guardados correctamente. Los cambios pueden tardar unos minutos en reflejarse en la página.')
            return render(request, 'menu_perfil/informacion.html', {'title': 'Perfil', 'cantidad_carrito': cantidad_carrito})
    else:
        form = PerfilForm()
    return render(request, 'menu_perfil/configuracion.html', {'title': 'Perfil', 'form': form, 'cantidad_carrito': cantidad_carrito})

@login_required
def carrito(request):
    cantidad_carrito = DetallesCarrito.objects.filter(idCarrito__idPerfil=request.user).count()
    carrito, created = Carrito.objects.get_or_create(idPerfil=request.user)
    detalles = DetallesCarrito.objects.filter(idCarrito=carrito)
    suma = 0
    for detalle in detalles:
        suma = suma + (detalle.idProducto.Precio * detalle.Cantidad)
    return render(request, 'carrito.html', {'title': 'Carrito', 'detalles': detalles, 'total': suma, 'cantidad_carrito': cantidad_carrito})

@login_required
def agregar_al_carrito(request, id):
    producto = Producto.objects.get(pk=id)
    carrito, created = Carrito.objects.get_or_create(idPerfil=request.user)
    detalles = DetallesCarrito.objects.filter(idCarrito=carrito)
    for detalle in detalles:
        if detalle.idProducto == producto:
            detalle.Cantidad += 1
            detalle.save()
            return redirect('tienda')
    DetallesCarrito.objects.create(Cantidad=1, idProducto=producto, idCarrito=carrito)
    return redirect('tienda')

@login_required
def perfil(request):
    cantidad_carrito = DetallesCarrito.objects.filter(idCarrito__idPerfil=request.user).count()
    return render(request, 'menu_perfil/informacion.html', {'title': 'Perfil', 'cantidad_carrito': cantidad_carrito})

@login_required
def info(request):
    cantidad_carrito = DetallesCarrito.objects.filter(idCarrito__idPerfil=request.user).count()
    return render(request, 'menu_perfil/informacion.html', {'title': 'Perfil', 'cantidad_carrito': cantidad_carrito})

@login_required
def facturas(request):
    cantidad_carrito = DetallesCarrito.objects.filter(idCarrito__idPerfil=request.user).count()
    ordenes = Orden.objects.filter(idPerfil=request.user)
    return render(request, 'menu_perfil/facturacion.html', {'title': 'Perfil', 'facturacion': ordenes, 'cantidad_carrito': cantidad_carrito})

@login_required
def facturacion(request):
    carrito = get_object_or_404(Carrito, idPerfil=request.user)
    if carrito == None:
        return redirect('carrito')
    else:
        orden = generar_pdf_factura(request)
        correo = request.user.email
        nombre = request.user.first_name
        mail = create_mail(
            correo,
            'Genial, se ha realizado tu compra correctamente!',
            'correos/factura_pdf.html',
            {
                'user': nombre
            },
            orden.ArchivoPDF.path
            )
        mail.send(fail_silently=False)
        return redirect('carrito')

def create_mail(user_mail, subject, template_name, context, pdf=None):
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
    if pdf:
        message.attach_file(pdf)
    
    return message

def generar_pdf_factura(request):
    usuario = request.user
    carrito = get_object_or_404(Carrito, idPerfil=usuario)
    detalles_carrito = DetallesCarrito.objects.filter(idCarrito=carrito)

    # Calcular el total de la factura
    total = sum(detalle.Cantidad * detalle.idProducto.Precio for detalle in detalles_carrito)

    # Crear una nueva orden
    nueva_orden = Orden.objects.create(
        Fecha=date.today(),
        Total=total,
        Estado=True,  # O False, dependiendo de tu lógica de negocio
        idPerfil=usuario  # Asumiendo que el perfil del usuario se llama 'perfil'
    )

    # Ruta donde se guardará el PDF en el servidor
    factura_filename = f"factura_{nueva_orden.idOrden}_User_{usuario.id}_Name_{usuario.first_name}{usuario.last_name}.pdf"
    factura_directory = os.path.join(settings.MEDIA_ROOT, 'facturas', date.today().strftime('%Y/%m/%d'))
    os.makedirs(factura_directory, exist_ok=True)
    factura_filepath = os.path.join(factura_directory, factura_filename)

    # Crear el objeto Canvas y guardar el PDF en el servidor
    doc = SimpleDocTemplate(factura_filepath, pagesize=letter)
    story = []

    # Logo de la empresa (imagen)
    logo_path = os.path.join(settings.MEDIA_ROOT, 'B2C.png')  # Ruta de la imagen del logo
    logo = Image(logo_path, width=100, height=100)
    story.append(logo)

    # Título y datos de la empresa
    styles = getSampleStyleSheet()
    title = Paragraph("<b>Factura</b>", styles['Title'])
    story.append(title)

    # Información de la empresa
    info_empresa = [
        ("Nombre de la Empresa", "B2C Store"),
        ("Dirección", "..."),
        ("Teléfono", "+123456789"),
        ("Correo Electrónico", "b2c.contact.mvp@gmail.com"),
        # Puedes agregar más información aquí
    ]
    for key, value in info_empresa:
        info = Paragraph(f"<b>{key}:</b> {value}", styles['Normal'])
        story.append(info)

    # Separador
    story.append(Paragraph("<br/>", styles['Normal']))

    # Título y datos del usuario
    usuario_info = [
        ("Nombre de Usuario", usuario.username),
        ("Fecha", nueva_orden.Fecha.strftime('%d/%m/%Y')),
        # Puedes agregar más información aquí
    ]
    for key, value in usuario_info:
        info = Paragraph(f"<b>{key}:</b> {value}", styles['Normal'])
        story.append(info)

    # Separador
    story.append(Paragraph("<br/>", styles['Normal']))

    # Tabla de productos
    data = [["Producto", "Cantidad", "Precio Unitario", "Total"]]
    for detalle in detalles_carrito:
        nombre_producto = detalle.idProducto.Nombre
        cantidad = str(detalle.Cantidad)
        precio_unitario = f"${detalle.idProducto.Precio:.2f}"
        total_producto = f"${detalle.Cantidad * detalle.idProducto.Precio:.2f}"
        data.append([nombre_producto, cantidad, precio_unitario, total_producto])

    table = Table(data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

    story.append(table)

    # Total
    total_text = Paragraph(f"<b>Total:</b> ${total:.2f}", styles['Normal'])
    story.append(total_text)

    # Construir el PDF
    doc.build(story)

    # Asignar el archivo PDF a la orden y guardar
    nueva_orden.ArchivoPDF.name = os.path.join('facturas', date.today().strftime('%Y/%m/%d'), factura_filename)
    nueva_orden.save()

    # Leer el archivo y devolverlo como respuesta HTTP
    with open(factura_filepath, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{factura_filename}"'

    carrito.delete()  # Eliminar el carrito

    return nueva_orden