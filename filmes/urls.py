from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'), 
    path('novo/', views.novo_filme, name='cadastrar_filme'),
    path('editar/<int:id>/', views.editar_filme, name='editar_filme'),
    path('excluir/<int:id>/', views.excluir_filme, name='excluir_filme'),
]

