from django.urls import path
from . import views
from django.contrib import admin


admin.site.site_title = "TeekaYX | Admin"
admin.site.site_header = "TeekaYX | Administration"
admin.site.index_title = "Site administration"


urlpatterns = [
    path('courses/', views.course_list, name='course-list'),
    path('courses/<slug:slug>/', views.course_detail, name='course-detail'),
    path('courses/<slug:course_slug>/<slug:page_slug>/', views.course_page_detail, name='course-page-detail'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.policy, name='privacy-policy'),
    path('terms/', views.terms, name='terms'),
    path('contact-us/', views.contact, name='contact-us'),   
    path('', views.index, name='index'),
    


]
