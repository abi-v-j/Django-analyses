
from django.urls import path,include
from User import views
app_name="User"

urlpatterns = [
    # path('data',views.data,name="data"),
    path('dashboard/', views.dashboard, name='dashboard'),

]
