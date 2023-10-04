from django.urls import path
from .views import AllUser, ChangePasswordView, DeleteUser, RegistrationView,LoginView,LogoutView
from rest_framework_simplejwt import views as jwt_views

app_name = 'users'

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(), name='login'),
    path('all-user', AllUser.as_view(), name='login'),
    path('deleteUser/<str:username>', DeleteUser.as_view(), name='login'),
    path('accounts/change-password/', ChangePasswordView.as_view(), name='password'),
    path('accounts/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]