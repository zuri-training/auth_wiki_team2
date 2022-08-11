from django.urls import path
from authwiki_app import views

urlpatterns = [
    path('', views.index, name="index"), 
    path('service/', views.service, name="service"),
    path('faq/', views.Faq, name='faq'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('doc/', views.doc, name='doc'),
    path('text/', views.text, name='text'), 
    path('terms/', views.terms, name="terms"),
    path('disclamer/', views.disclamer, name="disclamer"),
    path('policy/',  views.policy, name='policy'),
    path('support/', views.support, name='support'),
    path('what_we_do/', views.what_we, name='what_we_do')
]


 