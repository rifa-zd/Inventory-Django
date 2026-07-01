from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')

def staff(request):
    return render(request, 'dashboard/staff.html')

def documents(request):
    documents = [
        {'name': 'Death Certificate', 'file_type': 'PDF', 'size': '24KB', 'uploaded_by': 'Thunder', 'date_added': '23rd Oct 2023', 'file_url': '#'},
        {'name': 'Murder Case Files', 'file_type': 'XLSX', 'size': '128KB', 'uploaded_by': 'Rain', 'date_added': '2nd Nov 2023', 'file_url': '#'},
    ]
    return render(request, 'dashboard/documents.html', {'documents': documents})

