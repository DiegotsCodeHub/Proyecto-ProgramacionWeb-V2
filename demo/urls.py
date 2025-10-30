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
from home import views  # <--- Debe ser exactamente así

urlpatterns = [
        path('admin/', admin.site.urls),

         path('', views.index, name='index'),
        path('Memo/', views.memorama_view, name='memorama'),
        path('static/Web/index.html', views.Web_view, name='web'),
        path('challenges/', views.challenges_view, name='challenges'),
        path('resources/', views.resources_view, name='resources'),
        path('solutions/', views.solutions_view, name='solutions'),
        path('take-action/', views.takeaction_view, name='take-action'),
        
        #css
        path('static/style/baseStyle.css', views.stilo_view, name='stilo'),
        path('static/style/layout.css', views.stilos_view, name='stilos'),









]


