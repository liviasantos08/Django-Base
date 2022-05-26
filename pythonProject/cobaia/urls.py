from django.contrib import admin
from django.urls import path


from app1 import views
from app1.views import PessoaList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Base.as_view(), name='base'),
    path('form/', views.PessoaCreate.as_view(), name='forms'),
    path('table/', PessoaList.as_view(), name='tabela')
]
