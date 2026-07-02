from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    autores = models.ManyToManyField(Autor, related_name="livros", blank=True)

    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    """Leitor da biblioteca (tabela Usuario do modelo relacional)."""
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nome


class Emprestimo(models.Model):
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="emprestimos")
    funcionario = models.ForeignKey("auth.User", on_delete=models.PROTECT, related_name="emprestimos")
    livros = models.ManyToManyField(Livro, related_name="emprestimos")

    def __str__(self):
        return f"Empréstimo #{self.pk} - {self.usuario}"


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mensagem = models.TextField()
    enviado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.enviado_em:%d/%m/%Y})"
