from django.urls import path, include
from django.contrib import admin
from mycontacts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show),
    path('add/', views.add),
    path('viewctt/<int:detail_id>/', views.viewctt, name="detail"),
    path('edit/<int:detail_id>/', views.editctt, name="edit"),
]