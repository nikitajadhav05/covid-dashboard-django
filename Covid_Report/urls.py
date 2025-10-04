from django.contrib import admin
from django.urls import path, include
from covid_app import views  # ✅ Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),  # custom login
    path('covid_report/', views.covid_report, name='covid_report'),
    #path('logout/', views.logout_view, name='logout'),
]


