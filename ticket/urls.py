from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import DetailView
urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:id>/',DetailView.as_view(), name='details'),
    path('my_tickets',views.my_ticket, name='my_ticket'),


    path('login/', views.loginUser, name='login'),
    path('signup/', views.createUser, name='signup'),
    path('logout/', views.logoutUser, name='logout'),

    path('dev/', views.developer_dashboard, name='dev'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
