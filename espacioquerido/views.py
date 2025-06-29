from django.shortcuts import render

def dashboard(request):
    context = {
        'page_title': 'Dashboard',
        'active_page': 'dashboard'
    }
    return render(request, 'base.html', context)

def properties(request):
    context = {
        'page_title': 'Propiedades',
        'active_page': 'properties'
    }
    return render(request, 'base.html', context)

def clients(request):
    context = {
        'page_title': 'Clientes',
        'active_page': 'clients'
    }
    return render(request, 'base.html', context)

def agents(request):
    context = {
        'page_title': 'Agentes',
        'active_page': 'agents'
    }
    return render(request, 'base.html', context)

def transactions(request):
    context = {
        'page_title': 'Transacciones',
        'active_page': 'transactions'
    }
    return render(request, 'base.html', context)  # Fixed typo here

def reports(request):
    context = {
        'page_title': 'Reportes',
        'active_page': 'reports'
    }
    return render(request, 'base.html', context)