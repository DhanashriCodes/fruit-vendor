
from django.urls import path
from . import views

urlpatterns = [
    path('fruit/',views.handleFruit),
    path('fruit/<int:id>/',views.handleFruit),
    path('basket/',views.handleBasket),
    path('basket/<int:id>/',views.handleBasket),
    path('owner/',views.handleOwner),
    path('owner/<int:id>/',views.handleOwner)
]
