from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    html= """<h1>Sistema Institucional</h1>

<p>Mini sistema acadêmico desenvolvido em Django.</p>

<ul>
    <li><a href="/sobre/">Sobre</a></li>
    <li><a href="/projetos/">Projetos</a></li>
    <li><a href="/contato/">Contato</a></li>
</ul>"""
    return HttpResponse(html)

def sobre(request):
    html = """<h1>Sobre o Projeto</h1>

<p>Este projeto foi criado para demostrar páginas internas no Django.</p>

<p>Aluno:</p>

<ul>
    <li>Vinicius Gabriel</li>
</ul>

<a href="/">Voltar</a>"""

    return HttpResponse(html)

def projetos(request):
    html = """<h1>Projetos da Instituição</h1>

<table border="1">
    <tr>
        <th>Projeto</th>
        <th>Descrição</th>
    </tr>

    <tr>
        <td>Sistema de Biblioteca</td>
        <td>\Controle de livros</td>
    </tr>

</table>

<a href="/">Voltar</a>"""

    return HttpResponse(html)

def contato(request):
    html = """<h1>Contato</h1>

<p>Email: viniciuspx89@gmail.com</p>
<p>Telefone: (81) 9.9999-8888</p>
<p>Instituição: Uninassau - Paulista</p>"""

    return HttpResponse(html)

