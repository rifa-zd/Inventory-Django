from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.utils import timezone
from datetime import timedelta

from .models import Document, DocumentLog


def index(request):
    last_24h = timezone.now() - timedelta(hours=24)

    total_count = Document.objects.count()
    inserted_count = DocumentLog.objects.filter(
        action=DocumentLog.ADDED, timestamp__gte=last_24h
    ).count()
    removed_count = DocumentLog.objects.filter(
        action=DocumentLog.REMOVED, timestamp__gte=last_24h
    ).count()
    recent_activity = DocumentLog.objects.order_by('-timestamp')[:10]

    context = {
        'total_count': total_count,
        'inserted_count': inserted_count,
        'removed_count': removed_count,
        'recent_activity': recent_activity,
    }
    return render(request, 'dashboard/index.html', context)


def staff(request):
    return render(request, 'dashboard/staff.html')


def documents(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        uploaded_by = request.POST.get('uploaded_by')
        file = request.FILES.get('file')

        if name and uploaded_by and file:
            Document.objects.create(name=name, uploaded_by=uploaded_by, file=file)

        return redirect('dashboard-documents')

    all_documents = Document.objects.all()
    return render(request, 'dashboard/documents.html', {'documents': all_documents})


@require_POST
def delete_document(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    doc.delete()
    return redirect('dashboard-documents')