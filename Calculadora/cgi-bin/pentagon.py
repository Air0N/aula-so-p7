import cgitb, cgi
import funções

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")
# instancia um form para receber dados do navegador
form = cgi.FieldStorage()
#---logica do script ---#

perimetro = float(form.getvalue('perimetro'))
apotema = float(form.getvalue('apotema'))
# calcular area
pentagono_area = perimetro * apotema
#--- HTML ---#
title = "Pentagono"
funções.print_header(title)
print("<h1>Pentagono</h1><hr>")
print("<p>Perimetro: {:.1f}".format(perimetro))
print("<p>Apótema: {:.1f}".format(apotema))
print("<p>Área do Pentagono: {:.1f}".format(pentagono_area))
print("<br><br>Clique <a href=\'../pentagono.html\'>aqui</a> para novo cálculo.")
funções.print_footer()