from django.urls import path, include
from django.contrib import admin
from mycontacts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show),
    path('add/', views.add),
    path('detail/<int:detail_id>/', views.ContactDetailView, name="detail"),
]