from django.conf.urls import url 
from step2 import views

urlpatterns = [ 
	#url(r'^about/',views.about, name='about'),
	url(r'^view_stuff/$', views.view_stuff, name='view_stuff'),
]
