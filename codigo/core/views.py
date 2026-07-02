from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect, render

from .models import Autor, Contato, Livro


class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ["titulo", "ano", "autores"]


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ["nome"]


class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = ["nome", "email", "mensagem"]


@login_required
def home(request):
    return render(request, "core/home.html", {"total_livros": Livro.objects.count()})


# ---------- CRUD de Livros ----------

@login_required
def livro_list(request):
    return render(request, "core/livro_list.html", {"livros": Livro.objects.prefetch_related("autores")})


@login_required
def livro_form(request, pk=None):
    livro = get_object_or_404(Livro, pk=pk) if pk else None
    form = LivroForm(request.POST or None, instance=livro)
    if form.is_valid():
        form.save()
        messages.success(request, "Livro salvo com sucesso.")
        return redirect("livro_list")
    return render(request, "core/livro_form.html", {"form": form, "livro": livro})


@login_required
def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        livro.delete()
        messages.success(request, "Livro excluído.")
        return redirect("livro_list")
    return render(request, "core/livro_delete.html", {"livro": livro})


# ---------- CRUD de Autores ----------

@login_required
def autor_list(request):
    return render(request, "core/autor_list.html", {"autores": Autor.objects.all()})


@login_required
def autor_form(request, pk=None):
    autor = get_object_or_404(Autor, pk=pk) if pk else None
    form = AutorForm(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        messages.success(request, "Autor salvo com sucesso.")
        return redirect("autor_list")
    return render(request, "core/autor_form.html", {"form": form, "autor": autor})


@login_required
def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        autor.delete()
        messages.success(request, "Autor excluído.")
        return redirect("autor_list")
    return render(request, "core/autor_delete.html", {"autor": autor})


# ---------- Consulta / pesquisa ----------

@login_required
def consulta(request):
    q = request.GET.get("q", "").strip()
    resultados = Livro.objects.prefetch_related("autores")
    if q:
        resultados = resultados.filter(Q(titulo__icontains=q) | Q(autores__nome__icontains=q)).distinct()
    return render(request, "core/consulta.html", {"q": q, "resultados": resultados})


# ---------- Contato ----------

def contato(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Mensagem enviada aos desenvolvedores. Obrigado!")
        return redirect("contato")
    return render(request, "core/contato.html", {"form": form})
