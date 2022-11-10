# django
from django.urls import path
# local
from . import views

app_name="home_app"

urlpatterns = [
    #
    path(
        '', 
        views.HomeView.as_view(), 
        name="index"
    ),
    path(
        'ejemplo', 
        views.VistaEmjemplo.as_view(), 
        name="ejemplo"
    ),
]