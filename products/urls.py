from django.urls import path
from . import views


app_name = "products"
urlpatterns = [
    path('market/', views.market, name="market")
]
