from django.urls import path
from . import views
app_name = 'usuario_pasajero'
urlpatterns =[
    path('',views.index,name='index'),
    path('<int:id>',views.view_usuario,name='view_usuario'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'), 
    path('delete/<int:id>/', views.borrar, name='borrar'),
]