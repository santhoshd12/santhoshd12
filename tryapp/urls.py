from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

app_name='tryapp'

urlpatterns = [
    path('',views.list,name="listurl"),
    path('<slug:val>',views.agepage,name="slugpage"),
    path('newpost/',views.newpost,name="newpt")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
