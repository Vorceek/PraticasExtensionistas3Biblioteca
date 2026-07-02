from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("livros/", views.livro_list, name="livro_list"),
    path("livros/novo/", views.livro_form, name="livro_novo"),
    path("livros/<int:pk>/editar/", views.livro_form, name="livro_editar"),
    path("livros/<int:pk>/excluir/", views.livro_delete, name="livro_excluir"),
    path("autores/", views.autor_list, name="autor_list"),
    path("autores/novo/", views.autor_form, name="autor_novo"),
    path("autores/<int:pk>/editar/", views.autor_form, name="autor_editar"),
    path("autores/<int:pk>/excluir/", views.autor_delete, name="autor_excluir"),
    path("consulta/", views.consulta, name="consulta"),
    path("contato/", views.contato, name="contato"),
    path("mensagens/", views.mensagens, name="mensagens"),
]
