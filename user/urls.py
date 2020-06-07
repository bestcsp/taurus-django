from django.urls import path
from django.contrib.auth.views import (LoginView,
                                        LogoutView,
                                        PasswordResetView,
                                        PasswordResetDoneView,
                                        PasswordResetConfirmView,
                                        PasswordResetCompleteView,
)
from . import views
urlpatterns = [
    path('register',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='users/logout.html'),name='logout'),

    path('password_reset/',PasswordResetView.as_view(
        template_name='users/passwordreset.html'),
        name='password_reset'),
    path('password_reset/done',PasswordResetDoneView.as_view(
        template_name='users/passwordresetdone.html'),
        name='password_reset_done'),
    path('password_reset-confirm/<uidb64>/<token>',PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password-reset-complete',PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),

    path('profile',views.profile,name='profile'),
]