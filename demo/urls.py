"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# demo/urls.py
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from home import views  # <--- Debe ser exactamente así

urlpatterns = [
        #Admin Site
        path('admin/', admin.site.urls),

        #Templates
        path('', views.login_view, name='login'),
        path('templates/game.html/', views.Web_view, name='web'),
        path('challenges/', views.challenges_view, name='challenges'),
        path('resources/', views.resources_view, name='resources'),
        path('solutions/', views.solutions_view, name='solutions'),
        path('profile/', views.profile_view, name='profile'),
        path('start/', views.index, name='index'),
        path('register/', views.register_view, name='register'),
        path('logout/', views.logout_view, name='logout'),
        
        #CSS + Static Files + JS
        path('static/style/baseStyle.css', views.baseStyle_view, name='baseStyle'),
        path('static/style/layout.css', views.layoutStyle_view, name='layoutStyle'),
        path('static/style/resources.css', views.resourcesStyle_view, name='resourcesStyle'),
        path('static/style/gameStyle.css', views.gameStyle_view, name='gameStyle'),
        path('static/style/forms.css', views.formsStyle_view, name='formsStyle'),

        #Authentication Views
        path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),
        path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
        path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
        path("verify/<uidb64>/<token>/", views.verify_account, name="verify_account"),
]


