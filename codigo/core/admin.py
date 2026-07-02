from django.contrib import admin

from .models import Autor, Contato, Emprestimo, Livro, Usuario

admin.site.register([Autor, Livro, Usuario, Emprestimo, Contato])
