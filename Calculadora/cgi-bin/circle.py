import cgitb, cgi
import math
import funções

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")
# instancia um form para receber dados do navegador
form = cgi.FieldStorage()
#--- logica do script ---#

raio = float(form.getvalue('raio'))
# calcular area
circulo_area = math.pi * math.pow(raio, 2)
#--- HTML ---#
title = "Círculo"
funções.print_header(title)
print("<h1>Circulo</h1><hr>")
print("<p>Raio: {:.1f}".format(raio))
print("<p>Area do circulo: {:.1f}".format(circulo_area))
print("<br><br>Clique <a href=\'../circulo.html\'>aqui</a> para um novo calculo.")
funções.print_footer()