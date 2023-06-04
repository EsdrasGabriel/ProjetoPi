from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import cadastro_usuario
from .models import anuncios_tbl
import hashlib


# Create your views here.

def screenLogin(request):
    if request.method == "GET":
        return render(request, "usuarios/login.html")
    elif request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("password")

        try:
            auth = cadastro_usuario.objects.get(email=email)
            if auth.senha == senha:
                hash_md5 = hashlib.md5()
                hash_md5.update(email.encode("utf-8"))
                hash_md5.update(senha.encode("utf-8"))
                token = hash_md5.hexdigest()

                script = """
                    <script>
                        localStorage.setItem('token', '{token}');
                        window.location.href = '/home/';
                    </script>
                """.format(token=token)
                return HttpResponse(script)
            else:
                return HttpResponse("Email ou Senha inválidos.")
        except cadastro_usuario.DoesNotExist:
            return HttpResponse("Email ou Senha inválidos.")


def screenCadastro(request):
    if request.method == "GET":
        return render(request, "usuarios/cadastro.html")
    else:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        cpf = request.POST.get("cpf")
        endereco = request.POST.get("endereco")

        usuarioCpf = cadastro_usuario.objects.filter(cpf=cpf).first()
        usuarioEmail = cadastro_usuario.objects.filter(email=email).first()

        if usuarioCpf:
            return HttpResponse("Já existe uma conta cadastrada com esse cpf.")
        if usuarioEmail:
            return HttpResponse("Já existe uma conta cadastrada com esse email.")

        usuario = cadastro_usuario(
            nome=nome, email=email, senha=senha, cpf=cpf, endereco=endereco
        )
        usuario.save()


def screenHome(request):
    anuncios = {"anuncios": anuncios_tbl.objects.all()}

    return render(request, "usuarios/home/home.html", anuncios)


def screenPerfil(request):
    return HttpResponse(render(request, "usuarios/perfil.html"))


def screenCriar(request):
    if request.method == "GET":
        return render(request, "usuarios/anuncios/criar/criarAnuncio.html")

    elif request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        requisitos = request.POST.get("requisitos")
        anuncio_tbl = anuncios_tbl(
            titulo=titulo, descricao=descricao, requisitos=requisitos
        )
        anuncio_tbl.save()

        return redirect("http://127.0.0.1:8000/perfil/")


def screenEditar(request):
    return render(request, "usuarios/anuncios/editar/editarAnuncio.html")


def screenEditarInfo(request):
    id = request.GET.get("id")
    if id is not None:
        info = anuncios_tbl.objects.get(id_anuncio=id)
        infoo = {
            "id": info.id_anuncio,
            "titulo": info.titulo,
            "descricao": info.descricao,
            "requisitos": info.requisitos,
        }
        return HttpResponse(
            render(request, "usuarios/anuncios/editar/editarInformacoes.html", infoo)
        )

    elif request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        requisitos = request.POST.get("requisitos")
        id = int(request.POST.get("id"))

        infooo = anuncios_tbl.objects.filter(id_anuncio=id).first()
        infooo.titulo = titulo
        infooo.descricao = descricao
        infooo.requisitos = requisitos
        infooo.save()

        return redirect("http://127.0.0.1:8000/perfil/")

    else:
        return redirect("http://127.0.0.1:8000/perfil/EditarAnuncio/")


def screenDeletar(request):
    return render(request, "usuarios/anuncios/deletar/deletarAnuncio.html")


def screenConfirmacao(request):
    id = request.GET.get("id")
    if id is not None:
        info = anuncios_tbl.objects.get(id_anuncio=id)
        infoo = {
            "id": info.id_anuncio,
        }
        return HttpResponse(
            render(request, "usuarios/anuncios/deletar/confirmacao.html", infoo)
        )

    elif request.method == "POST":
        id = request.POST.get("id")
        delete = anuncios_tbl.objects.get(id_anuncio=id)
        delete.delete()

        return redirect("http://127.0.0.1:8000/perfil/")
    
    else:
        return render(request, "usuarios/anuncios/deletar/deletarAnuncio.html")


def screenExConta(request):
    if request.method == "GET":
        return render(request, "usuarios/excluirConta/excluirConta.html")
    elif request.method == "POST":
        senha = request.POST.get("password")
        email = request.POST.get("email")

        try:
            usuario = cadastro_usuario.objects.get(email=email)
            if usuario.senha == senha:
                usuario.delete()
                return redirect("http://127.0.0.1:8000/login/")
            else:
                return HttpResponse("Email ou senha incorretos.")
        except cadastro_usuario.DoesNotExist:
            return HttpResponse("Email ou senha invalidos")


def screenHomeFree(request):
    anuncios = {"anuncios": anuncios_tbl.objects.all()}

    return render(request, "usuarios/home/homeFree.html", anuncios)
