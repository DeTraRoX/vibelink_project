from django.urls import path
from django.contrib.auth import views as auth_views
from webapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),

    path('forget_pass/', views.forget_pass, name='forget_pass'),

    path('chat/', views.chat_view, name='chat_page'),
    path('chat_page/', views.chat_view, name='chats'),

    # Password reset flow
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='webapp/forget_pass.html'
    ), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='webapp/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='webapp/password_reset_complete.html'
    ), name='password_reset_complete'),

    # Friend suggestions and add friend
    path('suggestions/', views.suggest_friends, name='suggestions'),
    path('add-friend/<int:user_id>/', views.add_friend, name='add_friend'),

    # Alias for profile_suggest (important: add the name here)
    path('profile-suggest/', views.suggest_friends, name='profile_suggest'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
