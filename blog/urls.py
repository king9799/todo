from django.urls import path
from .views import *

urlpatterns = [
    path('home/', index, name='home'),
    path('', home, name=' '),
    path('<int:id>', edit, name='edit'),
    path('delete/<int:id>', delete, name='delete'),
    path('dashboard/', home1)

]
