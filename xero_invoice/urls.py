

from django.contrib import admin
from django.urls import path,include
from invoice import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('form/',views.form,name='form'),
	path('auth/',views.start_xero_auth_view, name ='auth'),
	path('',views.login,name='login'),
	path('xero/',views.some_view_which_calls_xero,name='xero'),
	path('callback/',views.process_callback_view,name='callback'),
	path('success/',views.success,name='success'),

]
