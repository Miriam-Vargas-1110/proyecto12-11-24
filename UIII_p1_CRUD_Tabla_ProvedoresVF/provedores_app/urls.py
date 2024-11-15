from django.urls import path
from provedores_app import views

urlpatterns = [
    path("", views.inicio_vista,name="inicio_vista"),
    path("registrarprovedores/",views.registrarprovedores,name="registrarprovedores"),
    path("seleccionarprovedores/<id>",views.seleccionarprovedores,name="seleccionarprovedores"),
    path("editarprovedores/",views.editarprovedores,name="editarprovedores"),
    path("borrarprovedores/<codigo>",views.borrarprovedores,name="borrarprovedores"),
    
]