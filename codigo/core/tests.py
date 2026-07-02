from django.contrib.auth.models import User
from django.test import TestCase

from .models import Autor, Contato, Livro


class SmokeTest(TestCase):
    def setUp(self):
        User.objects.create_user("admin", password="admin123")
        self.client.login(username="admin", password="admin123")

    def test_paginas_e_crud(self):
        # páginas principais
        for url in ["/", "/livros/", "/autores/", "/consulta/", "/contato/"]:
            self.assertEqual(self.client.get(url).status_code, 200)

        # sem login redireciona para /login/
        self.client.logout()
        self.assertEqual(self.client.get("/").status_code, 302)
        self.client.login(username="admin", password="admin123")

        # CRUD de livro
        self.client.post("/livros/novo/", {"titulo": "Teste", "ano": 2026})
        livro = Livro.objects.get(titulo="Teste")
        self.client.post(f"/livros/{livro.pk}/editar/", {"titulo": "Teste 2", "ano": 2026})
        self.assertTrue(Livro.objects.filter(titulo="Teste 2").exists())

        # consulta encontra o livro
        resp = self.client.get("/consulta/", {"q": "Teste 2"})
        self.assertContains(resp, "Teste 2")

        self.client.post(f"/livros/{livro.pk}/excluir/")
        self.assertFalse(Livro.objects.filter(pk=livro.pk).exists())

        # CRUD de autor
        self.client.post("/autores/novo/", {"nome": "Autor X"})
        autor = Autor.objects.get(nome="Autor X")
        self.client.post(f"/autores/{autor.pk}/editar/", {"nome": "Autor Y"})
        self.assertTrue(Autor.objects.filter(nome="Autor Y").exists())
        self.client.post(f"/autores/{autor.pk}/excluir/")
        self.assertFalse(Autor.objects.filter(pk=autor.pk).exists())

        # contato grava no banco
        self.client.post("/contato/", {"nome": "Ana", "email": "a@a.com", "mensagem": "Oi"})
        self.assertEqual(Contato.objects.count(), 1)

        # mensagens: usuario comum nao acessa, staff acessa
        self.assertEqual(self.client.get("/mensagens/").status_code, 302)
        User.objects.create_user("chefe", password="chefe123", is_staff=True)
        self.client.login(username="chefe", password="chefe123")
        resp = self.client.get("/mensagens/")
        self.assertContains(resp, "Ana")
