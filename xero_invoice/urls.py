

from django.contrib import admin
from django.urls import path,include
from invoice import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('form/',views.form,name='form'),
	path('auth/',views.start_xero_auth_view, name ='auth'),

]
