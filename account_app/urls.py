from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterView.as_view(), name="register-page"),
    path('login', views.LoginView.as_view(), name="login-page"),
    path('logout', views.LogoutView.as_view(), name="logout-page"),
    path('forget-password', views.ForgetPasswordView.as_view(), name="forgot-password-page"),
    path('reset-password/<active_code>', views.ResetPasswordView.as_view(), name="reset-password-page"),
    path('activate-account/<email_active_code>', views.ActivateAccountView.as_view(), name="activate-account")

]
