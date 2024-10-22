from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path("users/", views.UserListAPIView.as_view(), name="user-list"),
    path("users/<int:id>/", views.UserDetailAPIView.as_view(), name="user-detail"),
    path("users/<int:user_id>/address/", views.UserAddressListAPIView.as_view(), name="user-address-list"),
    path("users/<int:user_id>/address/<int:id>/", views.UserAddressDetailAPIView.as_view(), name="user-address-detail"),
    path("users/<int:user_id>/viewed_products/", views.ViewedProductListAPIView.as_view(), name="user-viewed-products"),

    path('verify-email/<str:email>/<uuid:code>/', views.EmailVerificationView.as_view(), name='email_verification'),
    path("auth/", views.UserTokenAuth.as_view(), name="auth"),
    path('auth/social-login/', views.SocialAuthAPIView.as_view(), name='social_login'),
    path('password_reset/', views.PasswordChangeRequestView.as_view(), name='reset_password_request'),
    path('password/', views.PasswordResetView.as_view(), name='password_changing'),
    path('contact_us/', views.ContactUsAPIView.as_view(), name='contact_us'),
]
