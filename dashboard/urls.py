from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('documents/', views.documents, name='dashboard-documents'),

    path('documents/<int:doc_id>/delete/', views.delete_document, name='dashboard-dlt-doc'),

]