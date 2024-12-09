# urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    # Add other paths as needed
    path('initiate-payment/', views.initiate_mpesa_payment, name='initiate_mpesa_payment'),
    path('callback/', views.mpesa_callback, name='mpesa_callback'),
    

   
]

