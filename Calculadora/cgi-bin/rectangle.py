import cgitb, cgi
import funções

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")
# instancia um form para receber dados do navegador
form = cgi.FieldStorage()
#--- logica do script ---#

# recebe o valor do raio do usuario
base = float(form.getvalue('base'))
altura = float(form.getvalue('altura'))
# calcular area
retangulo_area = base * altura
#--- HTML ---#
title = "Retângulo"
funções.print_header(title)
print("<h1>Retângulo</h1><hr>")
print("<p>Base: {:.1f}".format(base))
print("<p>Altura: {:.1f}".format(altura))
print("<p>Área do retângulo: {:.1f}".format(retangulo_area))
print("<br><br>Clique <a href=\'../retangulo.html\'>aqui</a> para um novo cálculo.")
funções.print_footer()
