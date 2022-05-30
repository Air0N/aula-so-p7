import cgitb, cgi
import funções

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")
# instancia um form para receber dados do navegador
form = cgi.FieldStorage()
#--- logica do script ---#

base = float(form.getvalue('base'))
altura = float(form.getvalue('altura'))
# calcular area
triangulo_area = (base * altura) / 2
############ HTML
title = "Pentagono"
funções.print_header(title)
print("<h1>Triangulo</h1><hr>")
print("<p>Base: {:.1f}".format(base))
print("<p>Altura: {:.1f}".format(altura))
print("<p>Área do Triangulo: {:.1f}".format(triangulo_area))
print("<br><br>Clique <a href=\'../triangle.html\'>aqui</a> para novo cálculo.")
funções.print_footer()