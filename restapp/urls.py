from django.urls import path
from . import views
from .views import userview

urlpatterns = [
    path('',views.home,name='home'),
    path('post_data',views.post_data,name='post_data'),
    path('delete',views.delete_data,name='delete'),
    path('class',userview.as_view(),name='classbased'),
    path('class/<int:id>',userview.as_view(),name='classdelete'),
    path('register',views.register,name='register'),
    path('loginview',views.loginview,name='loginview'),
    path('get_data',views.get_data,name='get_data'),

]

