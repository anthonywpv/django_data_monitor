from django.shortcuts import render
import requests
from django.conf import settings

# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import login_required

@login_required
@permission_required('dashboard.index_viewer', raise_exception=True)
def base(request):
    response = requests.get(settings.API_URL)  # URL de la API
    posts = response.json()  # Convertir la respuesta a JSON

    # Número total de respuestas
    total_responses = len(posts)

    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
    }

    return render(request, 'dashboard/index.html', data)