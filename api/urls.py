from django.urls import path
from . import views


urlpatterns = [
    path('v1/ingredients/', views.ingredients),
    path('v1/purchases/', views.purchases),
    path('v1/purchases/<int:recipe_id>/', views.remove_purchases),
]
