from django.urls import path, include
from .views import main, games, basket

urlpatterns = [
    path('', main, name='main'),
    path('games/', include('/games')),
    path('basket/', include('/basket')),
]