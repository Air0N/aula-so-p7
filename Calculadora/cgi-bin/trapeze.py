import cgitb, cgi
import funções

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")
# instancia um form para receber dados do navegador
form = cgi.FieldStorage()
#--- logica do script ---#

base_maior = float(form.getvalue('base maior'))
base_menor = float(form.getvalue('base menor'))
altura = float(form.getvalue('altura'))
# calcular area
trapezio_area = (base_maior + base_menor) * altura / 2
#--- HTML ---#
title = "Trapézio"
funções.print_header(title)
print("<h1>Trapézio</h1><hr>")
print("<p>Base Maior: {:.1f}".format(base_maior))
print("<p>Base Menor: {:.1f}".format(base_menor))
print("<p>Altura: {:.1f}".format(altura))
print("<p>Área do trapezio: {:.1f}".format(trapezio_area))
print("<br><br>Clique <a href=\'../trapezio.html\'>aqui</a> para novo cálculo.")
funções.print_footer()