from urllib.parse import urlparse
from django.urls import path
from authwiki_app import views

urlpatterns = [
    path('', views.index, name="index"), 
    path('service/', views.service, name="service"),
    path('social_proof/', views.social_proof, name="social_proof"),
    path('faq/', views.Faq, name='faq')
]


 