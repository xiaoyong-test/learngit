from django.urls import path
from App import views

app_name = 'App'
urlpatterns = [
    path('', views.index,name='index'),
    path('show/<name>/', views.show,name='show'),
    path('reverse/',views.reverse_url,name='reverse'),
    path('register/', views.register.name='register'),
    path("include/", views.include_div,name='include'),

    path("url/",views.handle_url,name='url'),
    path("extends/",views.handle_extend,name='extends'),
    path("jin/",views.load_jinja,name='jin'),
]