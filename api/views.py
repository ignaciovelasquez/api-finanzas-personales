from django.shortcuts import render

def bienvenida(request):
    contexto = {
        'titulo': 'API de Finanzas Personales',
        'descripcion': 'Servicio backend para la gestión de ingresos, egresos, presupuestos y control de cuentas.'
    }
    return render(request, 'bienvenida.html', contexto)