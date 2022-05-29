from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='mainpadge'),
    path('howto', views.howto, name='howto'),
    path('about', views.about, name='about'),
    path('retakeoff/<str:id>/', views.retakeoff, name='retakeoff'),
    path('delete_all_data', views.delete_all_data, name='delete_all_data'),
    path('delete_one_plane/<str:id>/', views.delete_one_plane, name='delete_one_plane'),
]